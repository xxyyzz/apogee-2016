# encoding=utf8
from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from Event.models import *
from backend.models import *
from django.views.decorators.csrf import csrf_exempt
import json
import html2text as gaussx
# Create your views here.
@csrf_exempt
def geteventdata(request,event_id):
	try:
		eventid = event_id
	except :
		raise Http404
	try :
		event=Event.objects.get(pk=eventid)
	except ObjectDoesNotExist:
		raise Http404
	# if request.GET:
	# 	eventid = request.GET['id']
	# 	try :
	# 		event=Event.objects.get(pk=eventid)
	# 	except ObjectDoesNotExist:
	# 		raise Http404
	resp = {}

	# resp['category']=unicode(event.category.name)
	# resp['content']=str(unicode(event.content))
	resp['eventname']=event.name
	resp['eventcategory']=str(unicode(event.category.name))
	resp['eventshortdescription']=unicode(event.short_description)

	resp['contact']=   str(  unicode(event.org.phone ) )
	resp['is_kernel']= str(unicode(event.is_kernel))
	resp['register']=    str(unicode(event.register) )

	# resp['eventdescription']=unicode(event.description)
	resp['tabs'] = [{k.heading.name : k.content} for k in event.tab_set.all()]
	resp['img']= str(unicode( event.img ))
	return JsonResponse(resp)

@csrf_exempt
def summary(request):
	response = []
	categories = EventCategory.objects.all()
	categories = [x for x in categories if x.name != "Other"]
	for category in categories:
		container = {}
		container['category'] = category.name
		eventlist = {}
		events = [
					{
						'id':event.id,
						'name':event.name,
						'short_desc':event.short_description,
						'tags':[tag.name for tag in event.tags.all()] + (['kernel'] if event.is_kernel else []),
					}
						for event in category.event_set.filter(is_displayed=True)
				]
		container['events'] = events
		response.append(container)
	return JsonResponse(response, safe=False)



def windows_json(request):
	resp={}
	resp['Groups'] =[]
	krn_events= Event.objects.filter(is_kernel= True)
	eve_cat= EventCategory.objects.all()
	gen_events= Event.objects.filter(is_kernel= False)


	temp = {}
	temp['UniqueId'] = "Events"
	temp['Title'] = "Events"
	temp['Items'] = []


	tempx={}
	tempx['UniqueId'] = "Kernel Events"
	tempx['Title'] = "Kernel Events"
	tempx['ImagePath'] = "Assets/LightGray.png"
	tempx['SubItems'] = []


	overview_ob  =Heading.objects.get(name='Overview')
	rules_ob  =Heading.objects.get(name='Rules')
	eligibility_ob  =Heading.objects.get(name='Eligibility')
	guidelines_ob  =Heading.objects.get(name='Guidelines')
	judging_ob  =Heading.objects.get(name='Judging Criteria')
	prob_ob  =Heading.objects.get(name='Problem Statements')
	resources_ob  =Heading.objects.get(name='Resources')
	sampleq_ob  =Heading.objects.get(name='Sample Questions')
	specifications_ob  =Heading.objects.get(name='Specifications')
	materials_ob  =Heading.objects.get(name='Materials')
	regdetails_ob  =Heading.objects.get(name='Registration Details')
	faqs_ob  =Heading.objects.get(name='FAQs')
	sponsors_ob  =Heading.objects.get(name='Sponsors')

	for k in krn_events:
		itemdict= {}
		itemdict["UniqueId"] = str(k.name).replace(' ','') + str(k.id)
		itemdict['Title'] = itemdict['UniqueId']
		itemdict['ImagePath'] = "Assets/"+ str(k.name.replace(" ","").lower() ) + ".png"
		try:
			itemdict['Overview'] = str(   gaussx.gaussx( str(Tab.objects.get(event=k, heading= overview_ob) ).content) )   )
		except:
			itemdict['Overview'] = ""
		try:
			itemdict['Rules'] = str(   gaussx.gaussx( str((Tab.objects.get(event=k, heading= rules_ob ) ).content) )   )
		except:
			itemdict['Rules'] = ""

		try:			
			itemdict['Eligibility'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= eligibility_ob) ).content )   )
		except:
			itemdict['Eligibility'] = ""

		try:			
			itemdict['Guidlines'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= guidelines_ob ) ).content )   )
		except:
			itemdict['Guidlines'] = ""

		try:			
			itemdict['Judging Criteria'] =str(    gaussx.gaussx((Tab.objects.get(event=k, heading= judging_ob) ).content )   )
		except:
			itemdict['Judging Criteria'] =""

		try:			
			itemdict['Problem Statements'] = str(    gaussx.gaussx((Tab.objects.get(event=k, heading= prob_ob)  ).content )  )
		except:
			itemdict['Problem Statements'] = ""


		try:			
			itemdict['Resources'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading=resources_ob) ).content )   )
		except:
			itemdict['Resources'] = ""

		try:
			itemdict['Sample Questions'] =str( gaussx.gaussx((Tab.objects.get(event=k, heading= sampleq_ob) ).content )   )
		except:
			itemdict['Sample Questions'] =""

		try:			
			itemdict['Specifications'] = str(  gaussx.gaussx((Tab.objects.get(event=k, heading= specifications_ob) ).content )   )
		except:
			itemdict['Specifications'] = ""

		try:			
			itemdict['Materials'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= materials_ob) ).content )   )
		except:
			itemdict['Materials'] = ""

		try:			
			itemdict['Registration Details'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= regdetails_ob) ).content )   )
		except:
			itemdict['Registration Details'] = ""

		try:			
			itemdict['FAQs'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= faqs_ob) ).content )   )
		except:
			itemdict['FAQs'] = ""

		try:			
			itemdict['Sponsors'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= sponsors_ob) ).content )   )
		except:
			itemdict['Sponsors'] = ""

		try:			
			itemdict['Contacts'] = str(   (Organization.objects.get(event=k) ).phone   )
		except:
			itemdict['Contacts'] = str(   (Organization.objects.get(event=k) ).phone   )



		tempx['SubItems'].append(itemdict)

	temp['Items'].append(tempx)

	for z in eve_cat:
		tempx={}
		tempx['UniqueId'] = str(z.name.replace(' ','')) + str(z.id)
		tempx['Title'] = tempx['UniqueId']
		tempx['SubItems'] = []
		for e_ob in Event.objects.filter(category=z,is_displayed=True):
			itemdict= {}
			itemdict["UniqueId"] = (str(e_ob.name).replace(' ','') + str(e_ob.id)).encode('ascii','ignore')
			itemdict['Title'] = itemdict['UniqueId']
			itemdict['ImagePath'] = "Assets/"+ str(e_ob.name.replace(" ","").lower() ) + ".png"
			try:
				itemdict['Overview'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= overview_ob) ).content )   )
			except:
				itemdict['Overview'] = ""
			try:
				itemdict['Rules'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= rules_ob ) ).content )   )
			except:
				itemdict['Rules'] = ""

			try:			
				itemdict['Eligibility'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= eligibility_ob) ).content )   )
			except:
				itemdict['Eligibility'] = ""

			try:			
				itemdict['Guidlines'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= guidelines_ob ) ).content )   )
			except:
				itemdict['Guidlines'] = ""

			try:			
				itemdict['Judging Criteria'] =str(    gaussx.gaussx((Tab.objects.get(event=k, heading= judging_ob) ).content )   )
			except:
				itemdict['Judging Criteria'] =""

			try:			
				itemdict['Problem Statements'] = str(    gaussx.gaussx((Tab.objects.get(event=k, heading= prob_ob)  ).content )  )
			except:
				itemdict['Problem Statements'] = ""


			try:			
				itemdict['Resources'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading=resources_ob) ).content )   )
			except:
				itemdict['Resources'] = ""

			try:
				itemdict['Sample Questions'] =str( gaussx.gaussx((Tab.objects.get(event=k, heading= sampleq_ob) ).content )   )
			except:
				itemdict['Sample Questions'] =""

			try:			
				itemdict['Specifications'] = str(  gaussx.gaussx((Tab.objects.get(event=k, heading= specifications_ob) ).content )   )
			except:
				itemdict['Specifications'] = ""

			try:			
				itemdict['Materials'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= materials_ob) ).content )   )
			except:
				itemdict['Materials'] = ""

			try:			
				itemdict['Registration Details'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= regdetails_ob) ).content )   )
			except:
				itemdict['Registration Details'] = ""

			try:			
				itemdict['FAQs'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= faqs_ob) ).content )   )
			except:
				itemdict['FAQs'] = ""

			try:			
				itemdict['Sponsors'] = str(   gaussx.gaussx((Tab.objects.get(event=k, heading= sponsors_ob) ).content )   )
			except:
				itemdict['Sponsors'] = ""

			try:			
				itemdict['Contacts'] = str(   (Organization.objects.get(event=k) ).phone   )
			except:
				itemdict['Contacts'] = str(   (Organization.objects.get(event=k) ).phone   )
			
			tempx['SubItems'].append(itemdict)
		temp['Items'].append(tempx)

	resp['Groups'].append(temp)

	



#############################################################################################
############### events end here : apart from events,(notable speakers n all) ################
#############################################################################################




	temp= {}
	temp['UniqueId'] = "ApartFromEvents"
	temp['Title'] = "ApartFromEvents"
	temp['Items'] = []


	tempx = {}
	tempx['UniqueId'] = "NotableSpeakers"
	tempx['Title']  =  "NotableSpeakers"
	tempx['ImagePath'] = ""
	tempx['SubItems'] = []


	itemdict={}
	itemdict["UniqueId"] = "Dr.Richard Stallman"
	itemdict['Title'] = "Dr.Richard Stallman"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = ""                                  ### content
	itemdict['Rules'] = "28 February"
	itemdict['Eligibility'] = ""
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)




	itemdict={}
	itemdict["UniqueId"] = "Dr.Richard Stallman"
	itemdict['Title'] = "Dr.Richard Stallman"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = """Dr. Richard Stallman launched the free software movement in 1983 and started the development of the GNU operating system in 1984 (which eventually helped develop Linux), and has been instrumental in the development of the GNU Project and the Free Software Foundation ever since. Richard developed a number of widely used programs that are components of GNU, including the original Emacs, the GNU Compiler Collection, the GNU symbolic debugger (gdb), GNU Emacs, and various others. He has been one of the most vociferous advocates of free software in his fight against software patents and dangerous extensions of copyright law.

The remarkable work undertaken by Dr. Stallman has been recognized worldwide and has led to him being awarded the ACM Grace Hopper Award, a MacArthur Foundation fellowship, the Electronic Frontier Foundation's Pioneer Award, and the the Takeda Award for Social/Economic Betterment, as well as several doctorates honoris causa.

Dr. Stallman will speak at the Think Again Conclave on 26th February about the burning issue of Net Neutrality vs Free Basics and why it is important to take the right side."""                                  ### content
	itemdict['Rules'] = "26 February"
	itemdict['Eligibility'] = ""
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)






	itemdict={}
	itemdict["UniqueId"] = "Mobasshar Javed Akbar"
	itemdict['Title'] = "Mobasshar Javed Akbar"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = """Since starting his career at the Times of India way back in 1971, Mobasshar Javed Akbar has gone on to become one of the most revered and exalted faces in the world of Indian journalism. Be it his work at Sunday, India's first political weekly, or the conception of The Telegraph, Mr. Akbar has redefined quality journalism at every stage of his career. He has deftly shouldered the onerous responsibility of being the editor in chief of Deccan Chronicle and The Sunday Guardian, and also pioneered the launch of Asian Age, India's first global newspaper.


He has authored some extremely insightful books, including Byline, Nehru: The Making of India, Kashmir: Behind the Vale, Riot After Riot and India: The Siege Within which have garnered praise from the critics and readers alike. His forays in the field of politics have seen him ease into the role of an accomplished statesman and have firmly established him as one of the leading voices on all social and political matters of the country."""                                  ### content
	itemdict['Rules'] = "27 February"
	itemdict['Eligibility'] = ""
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)









	itemdict={}
	itemdict["UniqueId"] = "Ashok Vajpeyi"
	itemdict['Title'] = "Ashok Vajpeyi"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = """Ashok Vajpeyi  (born 1941) is an Indian poet in Hindi, essayist, literary-cultural critic, apart from being a noted cultural and arts administrator, and a former civil servant. Noted for works like Kahin Nahin Wahin, Tatpurush, Bahuri Akela, Ibarat Se Giri Matrayen,among others , he has also published works on literary and art criticism like Filhal, Kuchh Poorvagrah, Samay se Bahar, Kavita ka Galp and Sidhiyan Shuru ho Gayi Hain. 
 He was chairman, Lalit Kala Akademi India's National Academy of Arts, Ministry of Culture, Govt of India, 2008–2011. He has published over 23 books of poetry, criticism and art, and was awarded the Sahitya Akademi Award given by Sahitya Akademi, India's National Academy of Letters, in 1994 for his poetry collection, Kahin Nahin Wahin.
He has also won the Dayavati Modi Kavi Shekhar Samman, 1994, and the Kabir Samman (2006) among others. """                                  ### content
	

	itemdict['Rules'] = "28 February"
	itemdict['Eligibility'] = ""
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)






	itemdict={}
	itemdict["UniqueId"] = "Rukmini Nair"
	itemdict['Title'] = "Rukmini Nair"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = """Rukmini Bhaya Nair is an eminent linguist, award winning poet, writer and critic of India. She won the First Prize for her poem Kali in the "All India Poetry Competition" in 1990 organised by The Poetry Society (India) in collaboration with British Council. She is currently a Professor at Humanities and Social Sciences department of the Indian Institute of Technology Delhi (IIT Delhi). Nair is known for being a trenchant critic of the Hindutva ideology and the religious and caste discrimination that it promotes.

Nair serves on the editorial boards of the International Journal of Literary Semantics (De Gruyter: Berlin & New York), The Journal of Multicultural Discourses (Multilingual Matters: London and Beijing); The Journal of Pragmatics (Elseiver: Amsterdam); Psychology & Social Practice (an e-journal) and The Macmillan Essential Dictionary among others. 

As the editor of Biblio, India's leading literary and cultural journal, she is also part of the Australian ABC Radio's panel of experts for its well-known program 'The Book Show'. In addition, she contributes to all major national dailies and magazines and is a frequent panellist on Mark Tully's BBC broadcast 'Something Understood'.

There is much to admire in Nair’s poetry: the technical refinement, the range of allusion and the verbal energy and ingenuity. It is intellectually rigorous poetry and Nair has no qualms about admitting it.

Nair's writings, both creative and critical, are taught on courses at universities such as Chicago, Toronto Kent, Oxford and Washington, and she contends that she writes poetry for the same reason that she does research in cognitive linguistics – to discover the limits of language.

Her awards and fellowships include J.N. Tata Scholarship, the Hornby Foundation Award and the Dorothy Lee Grant besides winning Poetry prizes of Poetry Society  """                                  ### content
	

	itemdict['Rules'] = "28 February"
	itemdict['Eligibility'] = ""
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)







	itemdict={}
	itemdict["UniqueId"] = "Anand Neelakantan"
	itemdict['Title'] = "Anand Neelakantan"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = """Anand Neelakantan is an Indian author from Kerala. His famous works include Asura: Tale of the Vanquished, Ajaya: Roll of the Dice andRise of Kali: Duryodhana's Mahabharata.
Asura: Tale of the Vanquished was Anand's debut novel. Upon release, it instantly topped the charts, and went on to become a best seller. His second book, Ajaya: Roll of the Dice, topped the best seller charts for sixteen consecutive weeks. Anand is known to have created a whole new genre in literature - the counter telling of mythological epics. Asura narrates the Ramayana from the perspective of its anti-hero,Ravana. Similarly, Ajaya portrays the Mahabharata from the perspective of the Kauravas.

Anand Neelakantan was rated as one of the most promising writers by the Indian Express, and was also featured as one of the six most remarkable writers of 2012 by DNA. Other than novels, he has written columns for Deccan Chronicle, Asian Age, The New Indian Expressand The Wall Street Journal. His book Asura has been translated into many languages, including Hindi, Tamil, Telugu, Malayalam, Kannada, Gujarati, Marathi and Italian. """                                  ### content
	itemdict['Rules'] = "28 February"
	itemdict['Eligibility'] = ""
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)	









	itemdict={}
	itemdict["UniqueId"] = "Ajay Chaturvedi"
	itemdict['Title'] = "Ajay Chaturvedi"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = """Ajay Chaturvedi is a social entrepreneur and author. He is an alumnus of BITS Pilani and the University of Pennsylvania School of Engineering and Applied Science. He is the founder of HarVa, a business process outsourcing organization. The organization aims to improve the lifestyle of rural India using innovative and practical techniques. It reflects his belief in the power of cost-effective innovation as a method of development across the world, especially in rural India.

Ajay's book, Lost Wisdom of the Swastika, was a runaway best seller. Based on a true account, it is an engaging story of a man trying to find himself amidst the intricacies of the world around him. 

Ajay was CNN IBN's Youth Icon of the year 2011. He has also been honoured as an Iconic Youth 2014 by Rotary International. He was felicitated by BITS Pilani as one of its 50 most inspiring alumni in 50 years. He is an ambassador of the Power of Youth initiative of Scotland. """                                  ### content
	
	itemdict['Rules'] = "28 February"
	itemdict['Eligibility'] = ""
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)







	temp['Items'].append(tempx)



######################################################################
######   NOTABLE SPEAKERS AND LITFEST END HERE WORKSHOP BELOW ########
######################################################################




	tempx= {}
	tempx['UniqueId'] = "Workshops"
	tempx['Title'] = "Workshops"
	tempx['ImagePath'] = ""
	tempx['SubItems'] = []

	itemdict={}
	itemdict["UniqueId"] = "Ethical Hacking"
	itemdict['Title'] = "Ethical Hacking"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = """The workshop will be taken by Mr Akshay Awasthi, the CEO of Authentic Techs. Akshay Awasthi is one of the country’s best Information Security & Cyber Crime Consultant. The young and dynamic Akshay has not only assisted in solving complicated cyber crime cases but has also played a key role in spreading awareness about information security and cyber crimes. Akshay has trained more than 8000 personnel globally which include students from various ﬁelds, professionals from companies like Microsoft, Cisco, Intel etc and cyber security personnel.
See more about Akshay Awasthi: http://authentictechs.com/akshay-awasthi-2/ """                                  ### content
	
	itemdict['Rules'] = "Authentic Techs"
	itemdict['Eligibility'] = "27-28 February"
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)





	itemdict={}
	itemdict["UniqueId"] = "Surface Computing"
	itemdict['Title'] = "Surface Computing"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = "See more about Authentic Techs: http://authentictechs.com//"                                  ### content
	itemdict['Rules'] = "Authentic Techs"
	itemdict['Eligibility'] = "26 February"
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)

	itemdict={}
	itemdict["UniqueId"] = "Android App Development"
	itemdict['Title'] = "Android App Development"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = "See more about Authentic Techs: http://authentictechs.com//"                                  ### content
	itemdict['Rules'] = "Authentic Techs"
	itemdict['Eligibility'] = "27-28 February"
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)


	itemdict={}
	itemdict["UniqueId"] = "Dr.Richard Stallman"
	itemdict['Title'] = "Dr.Richard Stallman"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = ""                                  ### content
	itemdict['Rules'] = "28 February"
	itemdict['Eligibility'] = ""
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)


	itemdict={}
	itemdict["UniqueId"] = "Financial Markets"
	itemdict['Title'] = "Financial Markets"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = """The workshop will be taken by Mr Karthikyean Vijayakumar. Karthikeyan (KK) is the Founder & CEO of Twenty19. A firm believer in new technologies, he works at the intersection of technology and business. He co-founded Deepam, an NGO that provides opportunities & access to the less- privileged children through education. Deepam currently reaches out to over 220 children every weekend, in Chennai – India. He is a keen sportsman – Runs marathons, Plays ultimate Frisbee for Chakraa & Cricket for RunsnWickets. He has run 3 Marathons and 14 half marathons, officially and has also run at state-level sprint competitions.
Karthikeyan holds a degree in mechanical engineering from BITS, Pilani (2000 Batch). He was awarded the BITS Global 30 under 30 award in 2009. """                                  ### content
	itemdict['Rules'] = "Twenty19"
	itemdict['Eligibility'] = "27 February"
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)



	itemdict={}
	itemdict["UniqueId"] = "Matlab"
	itemdict['Title'] = "Matlab"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = """The workshop will be taken by Mr Karthikyean Vijayakumar. Karthikeyan (KK) is the Founder & CEO of Twenty19. A firm believer in new technologies, he works at the intersection of technology and business. He co-founded Deepam, an NGO that provides opportunities & access to the less- privileged children through education. Deepam currently reaches out to over 220 children every weekend, in Chennai – India. He is a keen sportsman – Runs marathons, Plays ultimate Frisbee for Chakraa & Cricket for RunsnWickets. He has run 3 Marathons and 14 half marathons, officially and has also run at state-level sprint competitions.
Karthikeyan holds a degree in mechanical engineering from BITS, Pilani (2000 Batch). He was awarded the BITS Global 30 under 30 award in 2009. """                                  ### content
	itemdict['Rules'] = "Twenty19"
	itemdict['Eligibility'] = "27-28 February"
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)


	itemdict={}
	itemdict["UniqueId"] = "Context Capture"
	itemdict['Title'] = "Context Capture"
	itemdict['ImagePath'] = "Assets/ppl/ojas.png"
	itemdict['Overview'] = """ContextCapture is Bentley's first product release of the Acute3D software technology it acquired earlier this year. The software is ideally suited for any organization that could apply 3D models of real-world context to benefit infrastructure design, construction, or operations. 

Bentley is a global leader dedicated to providing architects, engineers, geospatial professionals, constructors, and owner-operators with comprehensive software solutions for advancing infrastructure. Founded in 1984, Bentley has more than 3,000 colleagues in over 50 countries, more than $600 million in annual revenues, and since 2006 has invested more than $1 billion in research, development, and acquisitions. """
	itemdict['Rules'] = "Bentley"
	itemdict['Eligibility'] = "27-28 February"
	itemdict['Guidlines'] = ""
	itemdict['Judging Criteria'] = ""
	itemdict['Problem Statements'] = ""
	itemdict['Resources'] = ""
	itemdict['Sample Questions'] = ""
	itemdict['Specifications'] = ""
	itemdict['Materials'] = ""
	itemdict['Registration Details'] = ""
	itemdict['FAQs'] = ""
	itemdict['Sponsors'] = ""
	itemdict['Contacts'] = ""

	tempx['SubItems'].append(itemdict)

	temp['Items'].append(tempx)
	resp['Groups'].append(temp)

	return HttpResponse(json.dumps(resp), content_type="application/json")
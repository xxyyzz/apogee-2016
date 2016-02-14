/*
QUESTION SET : 
   # num - serial number of the question
   # cat - one of the category : chemistry, physics, maths, logic
   # ques - Question text
   # ques_image - link to any image in question if there
   # options - set of options to the question
      # type - type of the option (image/text)
      # desc - if image then link, else text
   correct - correct option (0,1,2,3)
   scoring - marks to get on correct answer, wrong answer, unattempted (idiots !)

   Hope this is more than clear !!!
*/


var set =[  
   {  
      'num':1,
      'cat':'aptitude',
      'ques':' A rich man died. In his will, he has divided his gold coins among his 5 sons, 5 daughters and a manager. According to his will: First give one coin to manager. 1/5th of the remaining to the elder son. Now give one coin to the manager and 1/5th of the remaining to second son and so on... After giving coins to 5th son, divided the remaining coins among five daughters equally. All should get full coins. Find the minimum number of coins he has? ',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'3121'
         },
         {  
            'type':'text',
            'desc':'3122'
         },
         {  
            'type':'text',
            'desc':'3123'
         },
         {  
            'type':'text',
            'desc':'3124'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':2,
      'cat':'aptitude',
      'ques':'*Find the next number in the series 11 12 20 23 33 46 ..... ',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'60'
         },
         {  
            'type':'text',
            'desc':'57'
         },
         {  
            'type':'text',
            'desc':'67'
         },
         {  
            'type':'text',
            'desc':'70'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':3,
      'cat':'aptitude',
      'ques':' If today is Wednesday, what is one day before the day, after the day, three days after the day before yesterday?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Monday'
         },
         {  
            'type':'text',
            'desc':'Thrusday'
         },
         {  
            'type':'text',
            'desc':'Tuesday'
         },
         {  
            'type':'text',
            'desc':'Sunday'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':4,
      'cat':'aptitude',
      'ques':' A girl has a certain number of pets. All but two are dogs, all but two are cats and all but two are goats.',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'4'
         },
         {  
            'type':'text',
            'desc':'3'
         },
         {  
            'type':'text',
            'desc':'5'
         },
         {  
            'type':'text',
            'desc':'2'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':5,
      'cat':'aptitude',
      'ques':'To move a Safe, two cylindrical steel bars 7 inches in diameter are used as rollers. How far will the safe have moved forward when the rollers have made one revolution',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'20 inches'
         },
         {  
            'type':'text',
            'desc':'21 inches'
         },
         {  
            'type':'text',
            'desc':'19 inches'
         },
         {  
            'type':'text',
            'desc':'22 inches'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':6,
      'cat':'aptitude',
      'ques':' In training for a competition, you find that swimming downstream (with the current) in a river, you can swim 2 miles in 40 minutes, & upstream (against the current), you can swim 2 miles in 60 minutes. How long would it take you to swim a mile in still water?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'23 min'
         },
         {  
            'type':'text',
            'desc':'24 min'
         },
         {  
            'type':'text',
            'desc':'22 min'
         },
         {  
            'type':'text',
            'desc':'20 min'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':7,
      'cat':'aptitude',
      'ques':'A sheet of paper has statements numbered from 1 to 100. Statement N says "Exactly N of the statements on this sheet are false." How many statements are true?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'1'
         },
         {  
            'type':'text',
            'desc':'99'
         },
         {  
            'type':'text',
            'desc':'98'
         },
         {  
            'type':'text',
            'desc':'100'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':8,
      'cat':'aptitude',
      'ques':'*Next number in the series is 1, 2, 4, 13, 31, 112, ?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'224'
         },
         {  
            'type':'text',
            'desc':'222'
         },
         {  
            'type':'text',
            'desc':'220'
         },
         {  
            'type':'text',
            'desc':'226'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':9,
      'cat':'aptitude',
      'ques':'Ankit and Tejas divided a bag of Apples between them.<br> Tejas said, "It&#39;s not fair! You have 3 times as many Apples I have." Ankit said, "OK, I will give you one Apple for each year of your age." Tejas replied, "Still not fair. Now, you have twice as many Apples as I have." "Dear, that&#39;s fair enough as I am twice older than you.", said Ankit.<br> Ankit went to Kitchen to drink water. While Ankit was in Kitchen, Tejas took apples from Ankit&#39;s pile equal to Ankit&#39;s age plus one.<br> Who have more apples now?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Ankit'
         },
         {  
            'type':'text',
            'desc':'Tejas'
         },
         {  
            'type':'text',
            'desc':'Both have equal apples'
         },
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':10,
      'cat':'aptitude',
      'ques':'There is a 50m long army platoon marching ahead. The last person in the platoon wants to give a letter to the first person leading the platoon. So while the platoon is marching, he runs ahead, reaches the first person and hands over the letter to him and without stopping he runs and comes back to his original position. In the meantime the whole platoon has moved ahead by 50m. The question is how much distance did the last person cover in that time. Assuming that he ran the whole distance with uniform speed.',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'120'
         },
         {  
            'type':'text',
            'desc':'130'
         },
         {  
            'type':'text',
            'desc':'140'
         },
         {  
            'type':'text',
            'desc':'110'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':11,
      'cat':'automobile',
      'ques':'What is the basic difference B/W DOHC and SOHC?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Orientation of the rocker'
         },
         {  
            'type':'text',
            'desc':'Inertia'
         },
         {  
            'type':'text',
            'desc':'Elasticity of the linkage'
         },
         {  
            'type':'text',
            'desc':'Operating mechanism'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':12,
      'cat':'automobile',
      'ques':' Why is carbon added during vulcanization of tyre rubber(Select the closest possible answer)?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'To make it black in colour'
         },
         {  
            'type':'text',
            'desc':'To prevent decay of rubber due to Ozone+UV rays'
         },
         {  
            'type':'text',
            'desc':'To increase shear strength of the material'
         },
         {  
            'type':'text',
            'desc':'Both 2 and 3'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':13,
      'cat':'automobile',
      'ques':'Which engine layout is used by the fastest car on the planet as of 2015?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'W16'
         },
         {  
            'type':'text',
            'desc':'V12'
         },
         {  
            'type':'text',
            'desc':'V8'
         },
         {  
            'type':'text',
            'desc':'Inline 8'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':14,
      'cat':'automobile',
      'ques':'Which characteristic of wheel alignment is needed for straight line stability?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Toe-Out'
         },
         {  
            'type':'text',
            'desc':'Toe-In'
         },
         {  
            'type':'text',
            'desc':'Caster'
         },
         {  
            'type':'text',
            'desc':'King-Pin Inclination'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':15,
      'cat':'automobile',
      'ques':'Which region of the tire would wear faster due to higher value of the above mentioned characteristic(Refer to previous question-Question 14)?',

      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Outward edge'
         },
         {  
            'type':'text',
            'desc':'Center of the Ellipsoid patch'
         },
         {  
            'type':'text',
            'desc':'Inward edge'
         },
         {  
            'type':'text',
            'desc':'None of the Above'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':16,
      'cat':'automobile',
      'ques':'Temperature indicating system gives temperature of which of the following components:-',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Cylinder'
         },
         {  
            'type':'text',
            'desc':'Lubricant'
         },
         {  
            'type':'text',
            'desc':'Cooling water'
         },
         {  
            'type':'text',
            'desc':'Piston face'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':17,
      'cat':'automobile',
      'ques':'Petrol that detonates easily is called:-',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Unleaded petrol'
         },
         {  
            'type':'text',
            'desc':'High octane petrol'
         },
         {  
            'type':'text',
            'desc':'Low octane petrol'
         },
         {  
            'type':'text',
            'desc':'Blended gasoline'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':18,
      'cat':'automobile',
      'ques':'Which of the following causes the least noise when operated at high speeds:-',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Herringbone gear'
         },
         {  
            'type':'text',
            'desc':'Helical gear'
         },
         {  
            'type':'text',
            'desc':'Spur gear'
         },
         {  
            'type':'text',
            'desc':'Both 1 and 2 produce equal noise'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':19,
      'cat':'automobile',
      'ques':'Which component in a spark plug causes it to produce spark:-',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Alternator'
         },
         {  
            'type':'text',
            'desc':'Condenser'
         },
         {  
            'type':'text',
            'desc':'Discharge coil'
         },
         {  
            'type':'text',
            'desc':'None of the Above'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':20,
      'cat':'automobile',
      'ques':'Which of the following symptom is caused as a result of brake disc run out?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Ineffectiveness during braking'
         },
         {  
            'type':'text',
            'desc':'Rapid vibration during braking'
         },
         {  
            'type':'text',
            'desc':'Localized wearing of brake pads'
         },
         {  
            'type':'text',
            'desc':'Rapid wearing of brake pads'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':21,
      'cat':'mechanical',
      'ques':'Nothing is known about the material x. The color of the material is bluish green. On drilling it gives two chips in the two flutes. Vibrations observed during drilling are low. The chips formed are segmented in nature. (shown in image) guess the material x. ',
      'ques_img':'/2016/static/revengg/qimg/reverse_eng/q21.png',
      'options':[  
         {  
            'type':'text',
            'desc':'Mild steel'
         },
         {  
            'type':'text',
            'desc':'Cast iron'
         },
         {  
            'type':'text',
            'desc':'Aluminum'
         },
         {  
            'type':'text',
            'desc':'Stainless steel'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':22,
      'cat':'mechanical',
      'ques':'In aqua-ammonia and lithium-bromide water absorption refrigeration systems, the refrigerants are respectively',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Water and Lithium bromide'
         },
         {  
            'type':'text',
            'desc':'Water and Ammonia'
         },
         {  
            'type':'text',
            'desc':'Ammonia and Lithium bromide'
         },
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':23,
      'cat':'mechanical',
      'ques':'A process engineer wishes to generate poke-yoke system on diving watches. The deep-sea divers need a mechanism to time their ascent to surface, which is done in stops. Which of these simple mechanisms would generate the best result?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Isolation valve on wrist watch'
         },
         {  
            'type':'text',
            'desc':'A Pawl-Ratchet system on the rotating dial of a watch'
         },
         {  
            'type':'text',
            'desc':'Digital stopwatch'
         },
         {  
            'type':'text',
            'desc':'A Rack and Pinion mechanism on the watch '
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':24,
      'cat':'mechanical',
      'ques':' A student in his first year is drilling on a piece of aluminium. His drill bit has undergone a significant wear. The apex angle has decreased from 90 degrees. This results in-',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'increased production rate'
         },
         {  
            'type':'text',
            'desc':'increased production time '
         },
         {  
            'type':'text',
            'desc':'metal removal rate remains the same but the vibrations has decreased'
         },
         {  
            'type':'text',
            'desc':'none of the above'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':25,
      'cat':'mechanical',
      'ques':'In a countercurrent flow heat exchanger :',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'the fluids at each inlet are at their lowest temperatures'
         },
         {  
            'type':'text',
            'desc':'the fluids are at their highest temperature'
         },
         {  
            'type':'text',
            'desc':'one is at its highest temperature, the other is at its lowest'
         },
         {  
            'type':'text',
            'desc':'none of the above'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':26,
      'cat':'miscellaneous',
      'ques':'Which of the pairs is incorrectly matched<br><table><thead><tr><th colspan=2>Spacecraft</th><th>Purpose</th></tr></thead><tbody><tr><td>1. </td><td>Cassini-Huygens</td><td>Orbiting Venus and transmitting data back to earth </td></tr><tr><td>2. </td><td>Messenger</td><td>Mapping and investigating Mercury</td></tr><tr><td>3. </td><td>Voyager 1<td>Exploring outer solar system</td></tr></tbody></table><br>Select the correct codes:',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'1 only'
         },
         {  
            'type':'text',
            'desc':'2 and 3 only'
         },
         {  
            'type':'text',
            'desc':'1 and 3 only'
         },
         {  
            'type':'text',
            'desc':'2 only'
         },
         {  
            'type':'text',
            'desc':'All of the above'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':27,
      'cat':'miscellaneous',
      'ques':'Which of the following bodies are presided over by non members',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Lok sabha'
         },
         {  
            'type':'text',
            'desc':'Rajya sabha'
         },
         {  
            'type':'text',
            'desc':'Vidhan sabhas of various states'
         },
         {  
            'type':'text',
            'desc':'Both Vidhan Sabha and Rajya sabha'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':28,
      'cat':'miscellaneous',
      'ques':'“Golan Heights” area which sometimes comes into news is located in',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'South Asia '
         },
         {  
            'type':'text',
            'desc':'North Africa'
         },
         {  
            'type':'text',
            'desc':'Middle East '
         },
         {  
            'type':'text',
            'desc':'Central Africa'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':29,
      'cat':'miscellaneous',
      'ques':'Consider the following countries<ol type=1> <li>China <li>France <li>North Korea <li>Israel <li>Pakistan <li>Australia</ol> Which of the above are known as nuclear NPT countries?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'1, 2 and 5 only'
         },
         {  
            'type':'text',
            'desc':'1,2,4 and 6 only'
         },
         {  
            'type':'text',
            'desc':'1 and 2 only'
         },
         {  
            'type':'text',
            'desc':'3,4,5 only'
         },
         {  
            'type':'text',
            'desc':'4 and 5 only'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':30,
      'cat':'miscellaneous',
      'ques':'Who amongst the following is not a governor(or equivalent) of a central bank in the world',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Mario Draghi'
         },
         {  
            'type':'text',
            'desc':'Janet Yellen'
         },
         {  
            'type':'text',
            'desc':'Zhou Xiaochuan'
         },
         {  
            'type':'text',
            'desc':'Jim Yong Kim'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':31,
      'cat':'miscellaneous',
      'ques':'Which of the following countries was visited for a <b>bilateral</b> visit by Narendra Modi in 2015',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Malaysia'
         },
         {  
            'type':'text',
            'desc':'Singapore'
         },
         {  
            'type':'text',
            'desc':'USA'
         },
         {  
            'type':'text',
            'desc':'Turkey'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':32,
      'cat':'miscellaneous',
      'ques':'Which of the following became the Presidents or Prime Minister of their country in 2015 ',
      'ques_img':null,
      'options':[  
         {  
            'type':'image',
            'desc':'/2016/static/revengg/qimg/reverse_eng/q32a.png'
         },
         {  
            'type':'image',
            'desc':'/2016/static/revengg/qimg/reverse_eng/q32b.png'
         },
         {  
            'type':'image',
            'desc':'/2016/static/revengg/qimg/reverse_eng/q32c.png'
         },
         {  
            'type':'image',
            'desc':'/2016/static/revengg/qimg/reverse_eng/q32d.png'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':33,
      'cat':'miscellaneous',
      'ques':'Which of the following well known global personalities did not pass away in 2015',
      'ques_img':null,
      'options':[  
         {  
            'type':'image',
            'desc':'/2016/static/revengg/qimg/reverse_eng/q33a.png'
         },
         {  
            'type':'image',
            'desc':'/2016/static/revengg/qimg/reverse_eng/q33b.png'
         },
         {  
            'type':'image',
            'desc':'/2016/static/revengg/qimg/reverse_eng/q33c.png'
         },
         {  
            'type':'image',
            'desc':'/2016/static/revengg/qimg/reverse_eng/q33d.png'
         }
      ],
      'correct':3,

      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':34,
      'cat':'miscellaneous',
      'ques':'Which footballer was not a part of the FIFA World XI 2015',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Andres Iniesta '
         },
         {  
            'type':'text',
            'desc':'James Rodriguez'
         },
         {  
            'type':'text',
            'desc':'Paul Pogba'
         },
         {  
            'type':'text',
            'desc':'Luka Modric'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':35,
      'cat':'miscellaneous',
      'ques':'Which country became the first country to legalize same sex marriage by a <b>popular vote</b>',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Britain'
         },
         {  
            'type':'text',
            'desc':'Scotland'
         },
         {  
            'type':'text',
            'desc':'Ireland'
         },
         {  
            'type':'text',
            'desc':'USA'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':36,
      'cat':'miscellaneous',
      'ques':'Recently an uprising of the people called the “Arab Spring” began from which country',
      'ques_img':null,
      'options':[  
          {  
            'type':'text',
            'desc':'Egypt'
         },
         {  
            'type':'text',
            'desc':'Libya'
         },
         {  
            'type':'text',
            'desc':'Tunisia'
         },
         {  
            'type':'text',
            'desc':'Syria'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':37,
      'cat':'miscellaneous',
      'ques':'What is the correct sequence of following cities as one moves from north to south in south east Asia<br><ol type=1> <li>Bangkok <li>Hanoi <li>Jakarta <li>Singapore</ol><br> Pick the correct code', 'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'3-1-2-4'
         },
         {  
            'type':'text',
            'desc':'1-4-2-3'
         },
         {  
            'type':'text',
            'desc':'1-2-3-4'
         },
         {  
            'type':'text',
            'desc':'2-1-4-3'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':38,
      'cat':'miscellaneous',
      'ques':'Duodenum of human body is a part of:',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Excretory system'
         },
         {  
            'type':'text',
            'desc':'Digestive system'
         },
         {  
            'type':'text',
            'desc':'Nervous system'
         },
         {  
            'type':'text',
            'desc':'Reproductive system'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':39,
      'cat':'miscellaneous',
      'ques':'Who issues the “Global Economic Prospectus” report.',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'IMF'
         },
         {  
            'type':'text',
            'desc':'World Bank'
         },
         {  
            'type':'text',
            'desc':'US Federal Reserve'
         },
         {  
            'type':'text',
            'desc':'World Economic Forum'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
   {  
      'num':40,
      'cat':'miscellaneous',
      'ques':'40. Which of the following <b>sitting </b>Prime Ministers were awarded the Bharat Ratna<br><ol><li>Jawaharlal Nehru</li><li>Indira Gandhi</li><li>Rajiv Gandhi</li><li>A.B. Vajpayee</li></ol>Select the correct options.',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'1, 2, and 3 only'
         },
         {  
            'type':'text',
            'desc':'2, and 3 only'
         },
         {  
            'type':'text',
            'desc':'1 and 2 only'
         },
         {  
            'type':'text',
            'desc':'1 and 4 only'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0
      ]
   },
]
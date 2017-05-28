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
      'cat':'chemistry',
      'ques':' INSTRUCTIONS FOR Q 1 – Q 4<br><br>Read the following passage and answer the questions below (Q 1 - Q 4)<br><br>Psychrometric charts are experimentally determined values of relative humidity vs temperature plotted in a graph along with several other parameters. On the y axis, we are given moisture content per kg of dry air and on the x axis, we are given dry bulb temperature (in Fahrenheit). Adding to the above information, we define two types of temperatures while reading psychrometric charts, namely, dry bulb and wet bulb temperature.<br><br>The Dry Bulb temperature, usually referred to as air temperature, is the air property that is most common used. When people refer to the temperature of the air, they are normally referring to its dry bulb temperature.<br><br>The Wet Bulb temperature is the adiabatic saturation temperature. Wet Bulb temperature can be measured by using a thermometer with the bulb wrapped in wet muslin. This thermometer is then rotated in the air in a horizontal circle by winding on a thread (like the mechanics problem you’ve done in physics!!). Due to the centrifugal force and heat generated due to this act, the water begins to evaporate and after sometime reached saturation i.e. water no longer evaporated. The temperature at this point is noted and denoted as Wet bulb temperature and is always lower than dry bulb temperature.<br><br>The diagonally aligned lines (the one with higher slope) are the enthalpy curves. For a hypothetical system, we determine relative humidity content by interpolating the intersection of vertical wet bulb temperature line with top most parabolic curve on y axis.<br><br>Now answer the following questions assuming water to behave as an ideal gas.<br><br><b>Q1.</b> For 1 kg water at atmospheric pressure, calculate dry bulb temperature. (Take specific volume of water as inverse of density) (Density of water = 1000 kg/m<sup>3</sup>)',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/image5.gif',
      'options':[  
         {  
            'type':'text',
            'desc':'1.818 / R'
         },
         {  
            'type':'text',
            'desc':'0.00001818 / R'
         },
         {  
            'type':'text',
            'desc':'0.101 / R'
         },
         {  
            'type':'text',
            'desc':'0.0000101 / R'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':2,
      'cat':'chemistry',
      'ques':'For air at wet bulb temperature of 0<sup>o</sup>C and dry bulb temperature of 25<sup>o</sup>C, find relative humidity (kg of water vapor/kg of air).',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'0.0315'
         },
         {  
            'type':'text',
            'desc':'0.004'
         },
         {  
            'type':'text',
            'desc':'0.022'
         },
         {  
            'type':'text',
            'desc':'None of these'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':3,
      'cat':'chemistry',
      'ques':'Calculate the number of moles of water present in 2 kg air with relative humidity of 0.05.',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'55.55'
         },
         {  
            'type':'text',
            'desc':'5.55'
         },
         {  
            'type':'text',
            'desc':'0.10'
         },
         {  
            'type':'text',
            'desc':'1000'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':4,
      'cat':'chemistry',
      'ques':' During the calculation of wet bulb temperature, at a particular instant a water droplet of mass 10 mg flies off along the tangent when the height of experiment from ground is 20m. How far will it land if the radius of the circle is 1 meter and tension in string is 1 N?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'40 m'
         },
         {  
            'type':'text',
            'desc':'20 m'
         },
         {  
            'type':'text',
            'desc':'5 m'
         },
         {  
            'type':'text',
            'desc':'1 m'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':5,
      'cat':'chemistry',
      'ques':'INSTRUCTIONS FOR Q 5 – Q 8<br><br>Read the following passage and answer the questions below (Q 5 - Q 8). From Q 5 to Q 7, the marks allotment will be in Arithmetic progression with Q 5 carrying 3 marks and increasing at the rate of 1 mark per question till Q 7. This means, Q 5 carries 3 marks, Q 6 carries 4 marks and Q 7 carries 5 marks. Q 8 carries 3 marks only. NEGATIVE MARKS AWARDED PER QUESTION IS EQUAL TO POSITIVE MARKS ALLOTTED TO RESPECTIVE QUESTION.<br><br><b>Q5.</b> How many of the above are anti-aromatic compounds?',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/image6.png',
      'options':[  
         {  
            'type':'text',
            'desc':'1'
         },
         {  
            'type':'text',
            'desc':'2'
         },
         {  
            'type':'text',
            'desc':'3'
         },
         {  
            'type':'text',
            'desc':'4'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':6,
      'cat':'chemistry',
      'ques':'How many of the above are aromatic by Huckel’s rule?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'4'
         },
         {  
            'type':'text',
            'desc':'5'
         },
         {  
            'type':'text',
            'desc':'6'
         },
         {  
            'type':'text',
            'desc':'7'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':7,
      'cat':'chemistry',
      'ques':'How many of the above compounds are non-planar?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'1'
         },
         {  
            'type':'text',
            'desc':'2'
         },
         {  
            'type':'text',
            'desc':'3'
         },
         {  
            'type':'text',
            'desc':'4'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':8,
      'cat':'chemistry',
      'ques':' How many of the above compounds are aromatic ?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'4'
         },
         {  
            'type':'text',
            'desc':'5'
         },
         {  
            'type':'text',
            'desc':'6'
         },
         {  
            'type':'text',
            'desc':'7'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':9,
      'cat':'chemistry',
      'ques':'Standard electrode potential data are useful for understanding the sustainability of an oxidant in a redox titration. Some half-cell reactions and their standard potentials are given below:<br><br>Identify the only incorrect statement regarding the quantitative estimation of aqueous Fe(NO<sub>3</sub>)<sub>2</sub>.',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/image7.png',
      'options':[  
         {  
            'type':'text',
            'desc':'MnO<sub>4</sub><sup>-</sup> can be used in aqueous HCl'
         },
         {  
            'type':'text',
            'desc':'Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> can be used in aqueous HCl'
         },
         {  
            'type':'text',
            'desc':'MnO<sub>4</sub><sup>-</sup> can be used in aqueous H<sub>2</sub>SO<sub>4<sub>'
         },
         {  
            'type':'text',
            'desc':'Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> can be used in aqueous H<sub>2</sub>SO<sub>4</sub>.'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':10,
      'cat':'chemistry',
      'ques':'For the first order parallel reaction k1 and k2 are 4 and 2 min-1 respectively at 300 K. If the activation energies for the formation of B and C are respectively 30,000 and 38.314 joule/mol respectively. The temperature at which B and C will be obtained in equimolar ratio is',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/image8.png',
      'options':[  
         {  
            'type':'text',
            'desc':'757.48 K'
         },
         {  
            'type':'text',
            'desc':'378.31 K'
         },
         {  
            'type':'text',
            'desc':'600 K'
         },
         {  
            'type':'text',
            'desc':'None of these'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':11,
      'cat':'physics',
      'ques':'INSTRUCTIONS FOR Q 11 – Q 14<br><br>Read the following passage and answer the questions below (Q 11 - Q 14)<br><br>A direct current flows through the winding of a long cylindrical solenoid of radius R. This produces in it a uniform magnetic field of induction B. An electron flies into the solenoid along the radius between its turns (at right angles to the solenoid axis) at a velocity v. After a certain time, the electron deflected by the magnetic field leaves the solenoid. Given, m is the mass of the electron, r is the radius of the path of the electron in the solenoid, and t is the transit time of the electron in the solenoid.<br><br> What is the transit time of the electron in the solenoid?',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/image9.png',
      'options':[  
         {  
            'type':'text',
            'desc':'(2m/eB)tan<sup>-1</sup>(eBr/mv)'
         },
         {  
            'type':'text',
            'desc':'(2m/eB)tan<sup>-1</sup>(eBR/mv)'
         },
         {  
            'type':'text',
            'desc':'(2m/eB)tan<sup>-1</sup>(mv/eBR)'
         },
         {  
            'type':'text',
            'desc':'(2m/eB)tan<sup>-1</sup>(mv/eBr)'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':12,
      'cat':'physics',
      'ques':' What will be the magnitude of the velocity of the electron at the end of its trajectory?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'(v<sup>2</sup> + (evBt/m)<sup>2</sup>)<sup>(1/2)</sup>'
         },
         {  
            'type':'text',
            'desc':'v'
         },
         {  
            'type':'text',
            'desc':'v - (evB/m)t'
         },
         {  
            'type':'text',
            'desc':'v + (evB/m)t'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':13,
      'cat':'physics',
      'ques':'What will be the magnitude of the force experienced by the electron inside the solenoid?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'evB'
         },
         {  
            'type':'text',
            'desc':'mv<sup>2</sup>/R'
         },
         {  
            'type':'text',
            'desc':'both (a) and (b) '
         },
         {  
            'type':'text',
            'desc':'neither (a) nor (b)'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':14,
      'cat':'physics',
      'ques':'If the solenoid is considerably long, the magnetic field produced by it would be',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'non-zero inside as well as outside the solenoid'
         },
         {  
            'type':'text',
            'desc':'zero outside, non-zero inside and along the axis of the solenoid '
         },
         {  
            'type':'text',
            'desc':'zero outside, non-zero inside but not along the axis of the solenoid'
         },
         {  
            'type':'text',
            'desc':'non-zero outside, non- zero inside but not exactly along the axis of the solenoid as there would be a non-zero component not oriented along the axis'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -3,
         0.5
      ]
   },
   {  
      'num':15,
      'cat':'physics',
      'ques':'INSTRUCTIONS FOR Q 15 – Q 18<br><br>Read the following passage and answer the questions below (Q 15 - Q 18)<br><br>A bird in air is diving vertically over a tank with speed 5cm/sec. Base of the tank is silvered. A fish in the tank is rising upward along the same line with speed 2cm/sec. Water level is falling at the rate of 2cm/sec. [µ<sub>water</sub> = 4/3, answer in cm/sec] <br><br> Speed of the image of the fish as seen by the bird directly is',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'8'
         },
         {  
            'type':'text',
            'desc':'6 '
         },
         {  
            'type':'text',
            'desc':'3'
         },
         {  
            'type':'text',
            'desc':'4'
         }
      ],
      'correct':1,
      'scoring':[  
         4,
         -4,
         0.5
      ]
   },
   {  
      'num':16,
      'cat':'physics',
      'ques':'Speed of the image of the fish formed after reflection in the mirror as seen by the bird is ?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'8'
         },
         {  
            'type':'text',
            'desc':'6'
         },
         {  
            'type':'text',
            'desc':'3'
         },
         {  
            'type':'text',
            'desc':'4'
         }
      ],
      'correct':2,
      'scoring':[  
         5,
         -5,
         0.5
      ]
   },
   {  
      'num':17,
      'cat':'physics',
      'ques':'Speed of the image of the bird relative to the fish looking upwards is ? ',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'8'
         },
         {  
            'type':'text',
            'desc':'6'
         },
         {  
            'type':'text',
            'desc':'3'
         },
         {  
            'type':'text',
            'desc':'4'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':18,
      'cat':'physics',
      'ques':'Speed of the image of the bird relative to the fish looking downwards in the mirror is ? ',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'8'
         },
         {  
            'type':'text',
            'desc':'6'
         },
         {  
            'type':'text',
            'desc':'3'
         },
         {  
            'type':'text',
            'desc':'4'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':19,
      'cat':'physics',
      'ques':'Determine the resistance RAB between points A and B of the frame made of thin homogeneous wire assuming that the number of successively embedded equilateral triangles (with sides decreasing by half) tends to infinity. Side AB is equal to "a" and the resistance of the unit length of the wire is equal to λ',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/image10.jpeg',
      'options':[  
         {  
            'type':'text',
            'desc':'aλ(√5 - 1)/3'
         },
         {  
            'type':'text',
            'desc':'aλ(√5 + 1)/3'
         },
         {  
            'type':'text',
            'desc':'aλ(√7 + 1)/3'
         },
         {  
            'type':'text',
            'desc':'aλ(√7 - 1)/3'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':20,
      'cat':'physics',
      'ques':'A nucleus of mass M + ∆m is at rest and decays into two daughter nuclei of mass M/2 each. Speed of daughter nuclei is (speed of light is c)',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'c√(Δm/M)'
         },
         {  
            'type':'text',
            'desc':'cΔm/(M+Δm)'
         },
         {  
            'type':'text',
            'desc':'c√(2Δm/M)'
         },
         {  
            'type':'text',
            'desc':'c√(Δm/(M+Δm)'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':21,
      'cat':'mathematics',
      'ques':'INSTRUCTIONS FOR Q 21 – Q 24<br><br>Read the following passage and answer the questions below (Q 21 - Q 24)<br><br>Two players A and B toss an unbiased coin in the cyclic order A, A, B, A, A, B … till a head appears. Let ‘X’ = a/b denotes the probability that A gets the head first and ‘Y’ that of B.<br><br> Find the number of positive integral values of c for which the equation ax<sup>2</sup> + bx + c = 0 has real solutions. (c ∈ R)',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'2'
         },
         {  
            'type':'text',
            'desc':'0'
         },
         {  
            'type':'text',
            'desc':'3'
         },
         {  
            'type':'text',
            'desc':'13'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':22,
      'cat':'mathematics',
      'ques':'',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/qpic22.jpg',
      'options':[  
         {  
            'type':'text',
            'desc':'7e<sup>5</sup>'
         },
         {  
            'type':'text',
            'desc':'6e<sup>5</sup>'
         },
         {  
            'type':'text',
            'desc':'3e<sup>5</sup>'
         },
         {  
            'type':'text',
            'desc':'5e<sup>5</sup>'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':23,
      'cat':'mathematics',
      'ques':'During APOGEE, the technical fest of BITS Pilani, 8 teams reached the finals of an event called RoboWars. To decide the winner, a tournament ladder was designed as shown below. Teams are paired and the winner emerges to the subsequent rounds. Teams A and B are also present. What is the chance that A and B encounter each other?',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/image11.png',
      'options':[  
         {  
            'type':'text',
            'desc':'1/(b-3)'
         },
         {  
            'type':'text',
            'desc':'(a-2)/b'
         },
         {  
            'type':'text',
            'desc':'1/2'
         },
         {  
            'type':'text',
            'desc':'1/7'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -3,
         0.5
      ]
   },
   {  
      'num':24,
      'cat':'mathematics',
      'ques':'Consider the triangle ABC shown in the figure. a, b, c represent the lengths of the sides opposite to vertices A, B, C respectively. ‘a’ and ‘b’ are the same as that mentioned in the paragraph. AD is the median. ∠C = 60<sup>o</sup>. Find the value of √(b<sup>2</sup> + c<sup>2</sup> + 2bc*cosA).',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/image12.png',
      'options':[  
         {  
            'type':'text',
            'desc':'√(43)'
         },
         {  
            'type':'text',
            'desc':'2√(43)'
         },
         {  
            'type':'text',
            'desc':'√(37)'
         },
         {  
            'type':'text',
            'desc':'2√(37)'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':25,
      'cat':'mathematics',
      'ques':'INSTRUCTIONS FOR Q 25 – Q 28<br><br>Read the following passage and answer the questions below (Q 25 - Q 28)<br><br>The gradient vector (gradient) of f(x, y) at a point P<sub>o</sub>(x<sub>o</sub>, y<sub>o</sub>) is the vector ∇f = (∂t/∂x)<b><i>i</i></b> + (∂t/∂y)<b><i>i</i></b> where (∂t/∂x) is the partial derivative of \'f\' w.r.t. \'x\' and (∂t/∂y) is the partial derivative of \'f\' w.r.t. \'y\'<br><br>The tangent plane at any point P<sub>o</sub>(x<sub>o</sub>, y<sub>o</sub>, z<sub>o</sub>) on a surface f(x, y, z) = c is perpendicular to ∇f at P<sup>o</sup> , i.e., ∇f is the normal line to the tangent plane at a surface.<br><br>If two surfaces touch each other at a point P<sub>o</sub>(x<sub>o</sub>, y<sub>o</sub>, z<sub>o</sub>), they will have a common tangent plane at that point, hence a common normal line, i.e., if i.e., if f(x,y,z) = c and g(x,y,z) = d  intersect at a point, then, ∇f = λ∇g at that point, here λ ∈ R. .<br><br>We use this to find the extreme values of a differentiable function f(x, y, z) subject to the constraint g(x, y, z) = 0 .<br><br>Now answer the questions that follow:<br><br>  What would be the gradient of one face of a tetrahedron with its three vertices being (1,0,0), (0,2,0) and (0,0,3)?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'i + 2j + 3k'
         },
         {  
            'type':'text',
            'desc':'i + j + k'
         },
         {  
            'type':'text',
            'desc':'i + j/2 + k/3'
         },
         {  
            'type':'text',
            'desc':'i + 3j + 2k'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':26,
      'cat':'mathematics',
      'ques':'  What would be the gradient of an ellipse with X- axis as its major axis, eccentricity e = 3/5 and length of major axis as 10, at the point (5, 4)?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'0.5i + 0.4j'
         },
         {  
            'type':'text',
            'desc':'0.4i + 0.5j'
         },
         {  
            'type':'text',
            'desc':'5i + 2j'
         },
         {  
            'type':'text',
            'desc':'2i + 5j'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':27,
      'cat':'mathematics',
      'ques':'  Find the point on the sphere x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup> = 4 which is farthest from the point (1, -1, 1)',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'( 1/√3 , -1/√3 , 1/√3 )'
         },
         {  
            'type':'text',
            'desc':'( -1/√3 , 2/√3 , -1/√3 )'
         },
         {  
            'type':'text',
            'desc':'( 2/√3 , -2/√3 , 2/√3 )'
         },
         {  
            'type':'text',
            'desc':'( -2/√3 , 2/√3 , -2/√3 )'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':28,
      'cat':'mathematics',
      'ques':' You are in charge of erecting a radio telescope on a newly discovered planet. To minimise interference, you want to place it where the magnetic field of the planet is weakest. The planet is spherical, with a radius of 6 units. Based on a coordinate system with the centre as origin, the strength of the magnetic field is given by M(x, y, z) = 6x − y<sup>2</sup> + xz + 60 . Where should you locate the telescope?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'(-4, 4, -2) '
         },
         {  
            'type':'text',
            'desc':'(-2, 2 4)'
         },
         {  
            'type':'text',
            'desc':'(-4, 4, 2) '
         },
         {  
            'type':'text',
            'desc':'(-2, 2, -4)'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':29,
      'cat':'mathematics',
      'ques':' A variable plane through a fixed point (1, 2, 3) cuts the coordinate axes in the point P, Q, R then locus of centre of sphere OPQR is (O is origin) ? ',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'(1/x) + (2/y) + (3/z) = 1'
         },
         {  
            'type':'text',
            'desc':'(1/x) + (2/y) + (3/z) = 2'
         },
         {  
            'type':'text',
            'desc':'x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup> = 4/9'
         },
         {  
            'type':'text',
            'desc':'x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup> = 1/9'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':30,
      'cat':'mathematics',
      'ques':' If | a + b + c | = √3; a, b, c are unit vectors, the maximum value of λ is',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'1/2'
         },
         {  
            'type':'text',
            'desc':'1'
         },
         {  
            'type':'text',
            'desc':'0'
         },
         {  
            'type':'text',
            'desc':'3'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':31,
      'cat':'logical reasoning',
      'ques':'Traditionally, decision making by doctors that is carefully, deductively reasoned has been considered preferable to intuitive decision making. However, a recent study found that senior surgeons used intuition significantly more than did most residents or mid-level doctors. This confirms the alternative view that intuition is actually more effective than careful, methodical reasoning. The conclusion above is based on which of the following assumptions?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Methodical, step-by-step reasoning is inappropriate for making many real-life medical decisions.'
         },
         {  
            'type':'text',
            'desc':'Senior surgeons have the ability to use either intuitive reasoning or deductive, methodical reasoning in making decisions.'
         },
         {  
            'type':'text',
            'desc':'The decisions that are made by mid-level and entry-level doctors can be made as easily by using methodical reasoning as by using intuitive reasoning.'
         },
         {  
            'type':'text',
            'desc':'Senior surgeons are more effective at decision making than are mid-level doctors.'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':32,
      'cat':'logical reasoning',
      'ques':" A drug that is very effective in treating some forms of cancer can, at present, be obtained only from the bark of the raynhu, a tree that is quite rare in the wild. It takes the bark of approximately 5,000 trees to make one pound of the drug. It follows, then, that continued production of the drug must inevitably lead to the raynhu's extinction. Which of the following, if true, most seriously weakens the above conclusion?" ,
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'The drug made from raynhu bark is dispensed to doctors from a central authority.'
         },
         {  
            'type':'text',
            'desc':'The drug made from the raynhu bark is expensive to produce.'
         },
         {  
            'type':'text',
            'desc':'The raynhu can be propagated from cuttings and cultivated by farmers. '
         },
         {  
            'type':'text',
            'desc':'The leaves of the raynhu are used in a large number of medical products.'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':33,
      'cat':'logical reasoning',
      'ques':'Complete the given sequence.<br><br>Z, W, S, P, L, I, E, ?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'B'
         },
         {  
            'type':'text',
            'desc':'D'
         },
         {  
            'type':'text',
            'desc':'F'
         },
         {  
            'type':'text',
            'desc':'K'
         }
      ],
      'correct':0,

      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':34,
      'cat':'logical reasoning',
      'ques':' In a code, CORNER is written as GSVRIV. How can CENTRAL be written in that code?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'DFOUSBM '
         },
         {  
            'type':'text',
            'desc':'GIRXVEP'
         },
         {  
            'type':'text',
            'desc':'GNFJKER'
         },
         {  
            'type':'text',
            'desc':'GJRYVEP'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':35,
      'cat':'logical reasoning',
      'ques':'  Pointing to a girl Sandeep said, "She is the daughter of the only sister of my father." How is Sandeep related to the girl?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Uncle'
         },
         {  
            'type':'text',
            'desc':'Cousin'
         },
         {  
            'type':'text',
            'desc':'Father'
         },
         {  
            'type':'text',
            'desc':'Grandfather'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':36,
      'cat':'logical reasoning',
      'ques':'',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/image13.png',
      'options':[  
         {  
            'type':'image',
            'desc':'/2016/static/aarohan/software/media/qimg/class12_setC/image14.png'
         },
         {  
            'type':'image',
            'desc':'/2016/static/aarohan/software/media/qimg/class12_setC/image15.png'
         },
         {  
            'type':'image',
            'desc':'/2016/static/aarohan/software/media/qimg/class12_setC/image16.png'
         },
         {  
            'type':'image',
            'desc':'/2016/static/aarohan/software/media/qimg/class12_setC/image17.png'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':37,
      'cat':'logical reasoning',
      'ques':' If banana is apple, apple is grapes, grapes is mango, mango is nuts, nuts is guava, which of the following is a yellow fruit?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Mango'
         },
         {  
            'type':'text',
            'desc':'Guava'
         },
         {  
            'type':'text',
            'desc':'Nuts'
         },
         {  
            'type':'text',
            'desc':'Apple'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':38,
      'cat':'logical reasoning',
      'ques':' a _ ba _ b _ b _ a _ b',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'abaab'
         },
         {  
            'type':'text',
            'desc':'abbab'
         },
         {  
            'type':'text',
            'desc':'bbabb'
         },
         {  
            'type':'text',
            'desc':'aabba'
         }
      ],
      'correct':2,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':39,
      'cat':'logical reasoning',
      'ques':' A man wears socks of two colours - Black and brown. He has altogether 20 black socks and 20 brown socks in a drawer. Supposing he has to take out the socks in the dark, how many must he take out to be sure that he has a matching pair? ',
      'ques_img':'',
      'options':[  
         {  
            'type':'text',
            'desc':'3'
         },
         {  
            'type':'text',
            'desc':'20 '
         },
         {  
            'type':'text',
            'desc':'39 '
         },
         {  
            'type':'text',
            'desc':'None of these '
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':40,
      'cat':'logical reasoning',
      'ques':'Find the missing character?',
      'ques_img':'/2016/static/aarohan/software/media/qimg/class12_setC/image18.png',
      'options':[  
         {  
            'type':'text',
            'desc':'7'
         },
         {  
            'type':'text',
            'desc':'25 '
         },
         {  
            'type':'text',
            'desc':'49 '
         },
         {  
            'type':'text',
            'desc':'129'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':41,
      'cat':'logical reasoning',
      'ques':' Synonym of ANTIPATHY is',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Enmity'
         },
         {  
            'type':'text',
            'desc':'Affection'
         },
         {  
            'type':'text',
            'desc':'Love'
         },
         {  
            'type':'text',
            'desc':'Good will'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':42,
      'cat':'logical reasoning',
      'ques':' Antonym of ZEALOT is',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Non-militant'
         },
         {  
            'type':'text',
            'desc':'Apathy'
         },
         {  
            'type':'text',
            'desc':'Liberal'
         },
         {  
            'type':'text',
            'desc':'Impious'
         }
      ],
      'correct':0,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':43,
      'cat':'logical reasoning',
      'ques':'INSTRUCTIONS FOR Q 43 TO Q 45.<br><br>Change the voice of each statement and choose the correct option.<br><br> I remember my sister taking me to the museum.',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'I remember I was taken to the museum by my sister.'
         },
         {  
            'type':'text',
            'desc':'I remember being taken to the museum by my sister.'
         },
         {  
            'type':'text',
            'desc':'I remember myself being taken to the museum by my sister.'
         },
         {  
            'type':'text',
            'desc':'I remember taken to the museum by my sister.'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':44,
      'cat':'logical reasoning',
      'ques':' Who is creating this mess?',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Who has been created this mess?'
         },
         {  
            'type':'text',
            'desc':'By whom has this mess been created?'
         },
         {  
            'type':'text',
            'desc':'By whom this mess is being created?'
         },
         {  
            'type':'text',
            'desc':'By whom is this mess being created?'
         }
      ],
      'correct':3,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   },
   {  
      'num':45,
      'cat':'logical reasoning',
      'ques':' They greet me cheerfully every morning',
      'ques_img':null,
      'options':[  
         {  
            'type':'text',
            'desc':'Every morning I was greeted cheerfully.'
         },
         {  
            'type':'text',
            'desc':'I am greeted cheerfully by them every morning.'
         },
         {  
            'type':'text',
            'desc':'I am being greeted cheerfully by them every morning.'
         },
         {  
            'type':'text',
            'desc':'Cheerful greeting is done by them every morning to me.'
         }
      ],
      'correct':1,
      'scoring':[  
         3,
         -1,
         0.5
      ]
   }
]
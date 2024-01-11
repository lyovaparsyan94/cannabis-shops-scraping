import os
import json
import pprint


def clean_data(list_of_circle_sections, store="aaa", address='bb'):
    final_data = {}
    for item in list_of_circle_sections:
        if str(item)[0].isdigit():
            if type(list_of_circle_sections[item]) is list:
                final_data[item] = list_of_circle_sections[item]
        if type(item) is dict:
            # if type(list_of_circle_sections[item]) is dict:
            for key, value in item.items():
                if key:
                    for k1, v1 in value.items():
                        max_distance = max(v1.keys())
                        if key not in final_data:
                            final_data[key] = {}
                        if k1 not in final_data[key]:
                            final_data[key][k1] = {}
                        final_data[key][k1][max_distance] = v1[max_distance]
    res = {}
    for price in final_data:
        if type(final_data[price]) is list:
            res = final_data
            break
        if price not in res:
            res[price] = []
            for degree in final_data[price]:
                for km in final_data[price][degree]:
                    res[price].append(final_data[price][degree][km])

    filename = str(store) + str(address)
    with open(f"gd_{filename}.json", 'w') as file:
        json.dump(res, file)
    pprint.pprint(res)
    return res


def write_report(global_data, store, address, status, url, ecom_provider, service_options, index):
    store_l = str(store).capitalize()
    address_l = str(address).capitalize()
    filename = store_l + address_l
    liner = f"\n{60 * '-'}\n"
    with open(f"{index}glob.txt", "w") as file:
        if not global_data:
            result = f"Delivery info for {store} at address {address} NOT Found from {ecom_provider} ecommerse provider's server"
            json.dump(result, file, indent=2)
        else:
            json.dump(global_data, file, indent=2)
    with open(f"{index}{filename}.txt", "a") as f:
        report = f"Store - {store}{liner}Address - {address}{liner}{status}{liner}URL {url}{liner}Platform - {ecom_provider}{liner}Service options\n{service_options}{liner}Delivery Zones according to the price\nfirst number is the price, and in brackets are the coordinates of area according to that price \n"
        f.write(report)
        with open(f'{index}glob.txt', 'r') as glob_file:
            for line in glob_file:
                f.write(line)
    os.remove(f'{index}glob.txt')


x = [
  {
    "0": {
      "0": {
        "0.5": [
          [
            43.662674122650856,
            -79.44141789999999
          ]
        ],
        "0.9": [
          [
            43.67077451445918,
            -79.44141789999999
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.68247506005931,
            -79.44141789999999
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.69777573725584,
            -79.44141789999999
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.71667651702311,
            -79.44141789999999
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.73917736350457,
            -79.44141789999999
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.76527823401194,
            -79.44141789999999
          ],
          "min order - 75.0"
        ],
        "3.3": [
          [
            43.79497907902427,
            -79.44141789999999
          ],
          "min order - 75.0"
        ]
      },
      "15": {
        "0.5": [
          [
            43.66252077008275,
            -79.43981350559274
          ]
        ],
        "0.9": [
          [
            43.67034511164867,
            -79.43692522053328
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.68164689592347,
            -79.43275247017125
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.696426087731226,
            -79.42729445665657
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.71468264548349,
            -79.42055015821207
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.73641652116815,
            -79.4125183282046
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.761627660338135,
            -79.40319749401318
          ],
          "min order - 75.0"
        ],
        "3.3": [
          [
            43.7903160021,
            -79.39258595569247
          ],
          "min order - 75.0"
        ]
      },
      "30": {
        "0.5": [
          [
            43.6620711653286,
            -79.43831847114186
          ]
        ],
        "0.9": [
          [
            43.669086175666635,
            -79.43273884949407
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.67921886561793,
            -79.42467803986375
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.69246916456568,
            -79.41413466066285
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.70883699663704,
            -79.4011069427862
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.728322280667605,
            -79.38559272817697
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.750924930165716,
            -79.36758946807782
          ],
          "min order - 75.0"
        ],
        "3.3": [
          [
            43.77664485327641,
            -79.34709422096523
          ],
          "min order - 75.0"
        ]
      },
      "45": {
        "0.5": [
          [
            43.6613559542908,
            -79.43703469770433
          ]
        ],
        "0.9": [
          [
            43.66708352648275,
            -79.42914418342627
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.675356501184496,
            -79.4177452082634
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.686174759429186,
            -79.40283617751344
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.699538178617196,
            -79.38441504963403
          ],
          "min order - 45.0"
        ],
        "2.5": [
          [
            43.715446632458736,
            -79.36247933490864
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.7338999909161,
            -79.33702609381726
          ],
          "min order - 75.0"
        ],
        "3.3": [
          [
            43.75489812014583,
            -79.30805193511011
          ],
          "min order - 75.0"
        ]
      },
      "60": {
        "0.5": [
          [
            43.66042388572651,
            -79.43604967851209
          ]
        ],
        "0.9": [
          [
            43.664473676242395,
            -79.42638623027207
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.67032310621241,
            -79.41242656060265
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.677972008423524,
            -79.39416928919267
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.68742021372443,
            -79.37161264949155
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.698667550964934,
            -79.34475448792448
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.7117138469352,
            -79.31359226292786
          ],
          "min order - 75.0"
        ]
      }
    }
  },
  {
    "0": {
      "72": {
        "0.5": [
          [
            43.65956439365034,
            -79.43552268124823
          ]
        ],
        "0.9": [
          [
            43.66206706243898,
            -79.42491084669528
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.66568171021184,
            -79.40958172146894
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.67040814003578,
            -79.38953436927807
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.67624615415353,
            -79.36476759220064
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.6831955539387,
            -79.3352799303969
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.691256139850736,
            -79.30106966174763
          ],
          "min order - 75.0"
        ]
      },
      "87": {
        "0.5": [
          [
            43.65840925595385,
            -79.43522791381284
          ]
        ],
        "0.9": [
          [
            43.65883265530973,
            -79.42408586036049
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.65944388348826,
            -79.40799161983713
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.660242725867676,
            -79.38694502617454
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.66122896777552,
            -79.36094586710449
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.66240239448031,
            -79.32999388421892
          ],
          "min order - 75.0"
        ]
      },
      "102": {
        "0.5": [
          [
            43.65723808987118,
            -79.43535498853328
          ]
        ],
        "0.9": [
          [
            43.65555339975171,
            -79.42444205297065
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.65311962326059,
            -79.40867956036045
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.64993655381198,
            -79.3880681585267
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.64600398464725,
            -79.36260867600795
          ],
          "min order - 75.0"
        ]
      },
      "117": {
        "0.5": [
          [
            43.656130707088764,
            -79.43589522183422
          ]
        ],
        "0.9": [
          [
            43.65245276594136,
            -79.42595500779555
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.64713990278176,
            -79.41159818636869
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.6401919425901,
            -79.39282604496447
          ],
          "min order - 45.0"
        ]
      },
      "132": {
        "0.5": [
          [
            43.65516256850122,
            -79.43681177910966
          ]
        ],
        "0.9": [
          [
            43.649742034203875,
            -79.42852150716836
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.641912171598406,
            -79.4165482251899
          ],
          "min order - 45.0"
        ]
      }
    }
  },
  {
    "0": {
      "144": {
        "0.5": [
          [
            43.65453308273934,
            -79.43777475864277
          ]
        ],
        "0.9": [
          [
            43.64797952224071,
            -79.43121781721523
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.638513134255064,
            -79.42174816665379
          ],
          "min order - 45.0"
        ]
      },
      "159": {
        "0.5": [
          [
            43.65397255542787,
            -79.43919672662234
          ]
        ],
        "0.9": [
          [
            43.646410096326115,
            -79.43519911616173
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.63548648173094,
            -79.4294258360367
          ],
          "min order - 45.0"
        ]
      },
      "174": {
        "0.5": [
          [
            43.65369832467613,
            -79.4407700329584
          ]
        ],
        "0.9": [
          [
            43.64564227758565,
            -79.43960402814116
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.63400574118604,
            -79.43792012398099
          ],
          "min order - 45.0"
        ]
      },
      "189": {
        "0.5": [
          [
            43.65372907495424,
            -79.44238748074973
          ]
        ],
        "0.9": [
          [
            43.645728375209934,
            -79.44413249444884
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.63417178052485,
            -79.44665258671412
          ],
          "min order - 45.0"
        ]
      },
      "204": {
        "0.5": [
          [
            43.65406271113146,
            -79.44393886750295
          ]
        ],
        "0.9": [
          [
            43.64666252367727,
            -79.4484760518978
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.63597328929573,
            -79.45502860085749
          ],
          "min order - 45.0"
        ]
      }
    }
  },
  {
    "0": {
      "216": {
        "0.5": [
          [
            43.65453308273934,
            -79.4450610413572
          ]
        ],
        "0.9": [
          [
            43.64797952224071,
            -79.45161798278475
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.638513134255064,
            -79.4610876333462
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.62613383019083,
            -79.47346848098401
          ],
          "min order - 45.0"
        ]
      },
      "231": {
        "0.5": [
          [
            43.65534171481005,
            -79.44623477925016
          ]
        ],
        "0.9": [
          [
            43.650243631824615,
            -79.45490442849866
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.642879515214,
            -79.46742572545439
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.63324922661655,
            -79.48379711429523
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.62135262519971,
            -79.50401660655855
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.607189567720965,
            -79.5280817822833
          ],
          "min order - 75.0"
        ]
      },
      "246": {
        "0.5": [
          [
            43.65634335328584,
            -79.44708030001547
          ]
        ],
        "0.9": [
          [
            43.65304816581209,
            -79.45727206275947
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.64828815566955,
            -79.47199233527844
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.642063139973374,
            -79.49123993482219
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.634372934917664,
            -79.51501334924413
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.625217355829896,
            -79.54331073752566
          ],
          "min order - 75.0"
        ]
      },
      "261": {
        "0.5": [
          [
            43.65746974582089,
            -79.44753997194789
          ]
        ],
        "0.9": [
          [
            43.65620203203321,
            -79.45855946964775
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.65437054848922,
            -79.47447603818804
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.65197508494343,
            -79.49528918522932
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.64901543107715,
            -79.52099828100886
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.64549137652305,
            -79.55160255836537
          ],
          "min order - 75.0"
        ]
      },
      "276": {
        "0.5": [
          [
            43.658644135309395,
            -79.44758244909217
          ]
        ],
        "0.9": [
          [
            43.65949031940524,
            -79.45867879331179
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.66071223932074,
            -79.47470717117922
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.662309681967535,
            -79.49566791345808
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.66428243411915,
            -79.52156144311816
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.66663028239447,
            -79.55238827530711
          ],
          "min order - 75.0"
        ]
      }
    }
  },
  {
    "0": {
      "288": {
        "0.5": [
          [
            43.65956439365034,
            -79.44731311875175
          ]
        ],
        "0.9": [
          [
            43.66206706243898,
            -79.4579249533047
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.66568171021184,
            -79.47325407853104
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.67040814003578,
            -79.49330143072191
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.67624615415353,
            -79.51806820779935
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.6831955539387,
            -79.54755586960309
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.691256139850736,
            -79.58176613825235
          ],
          "min order - 75.0"
        ],
        "3.3": [
          [
            43.70042771138969,
            -79.62070099858259
          ],
          "min order - 75.0"
        ]
      },
      "303": {
        "0.5": [
          [
            43.66062477915575,
            -79.44661657472187
          ]
        ],
        "0.9": [
          [
            43.665036188709514,
            -79.45597487444579
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.671407972636565,
            -79.46949384850048
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.67973997271222,
            -79.4871749531124
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.690032028450005,
            -79.5090200521128
          ],
          "min order - 45.0"
        ],
        "2.5": [
          [
            43.70228397703973,
            -79.535031417851
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.716495653285236,
            -79.5652117323144
          ],
          "min order - 75.0"
        ],
        "3.3": [
          [
            43.73266688954221,
            -79.59956408845629
          ],
          "min order - 75.0"
        ]
      },
      "318": {
        "0.5": [
          [
            43.66151814226849,
            -79.44556570735095
          ]
        ],
        "0.9": [
          [
            43.667537665002506,
            -79.45303250663459
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.67623236325906,
            -79.4638194405163
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.68760212817218,
            -79.47792809510379
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.70164684689894,
            -79.49536050103953
          ],
          "min order - 45.0"
        ],
        "2.5": [
          [
            43.718366402565344,
            -79.51611913490049
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.73776067421196,
            -79.54020692090678
          ],
          "min order - 75.0"
        ],
        "3.3": [
          [
            43.75982953673931,
            -79.56762723294102
          ],
          "min order - 75.0"
        ]
      },
      "333": {
        "0.5": [
          [
            43.66218359327555,
            -79.44423212776378
          ]
        ],
        "0.9": [
          [
            43.66940098415134,
            -79.44929834468154
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.679826016012804,
            -79.4566174804657
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.69345862673988,
            -79.46619082583484
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.710298748676884,
            -79.4780200335941
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.73034630860233,
            -79.49210712001603
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.75360122769843,
            -79.50845446652374
          ],
          "min order - 75.0"
        ]
      },
      "348": {
        "0.5": [
          [
            43.66257577476168,
            -79.44270672578308
          ]
        ],
        "0.9": [
          [
            43.67049913028983,
            -79.44502691734992
          ],
          "min order - 45.0"
        ],
        "1.3": [
          [
            43.681943942565894,
            -79.44837894217068
          ],
          "min order - 45.0"
        ],
        "1.7000000000000002": [
          [
            43.69691018101762,
            -79.45276344929385
          ],
          "min order - 45.0"
        ],
        "2.1": [
          [
            43.7153978085117,
            -79.45818126994583
          ],
          "min order - 75.0"
        ],
        "2.5": [
          [
            43.7374067813463,
            -79.46463341829656
          ],
          "min order - 75.0"
        ],
        "2.9": [
          [
            43.76293704924343,
            -79.47212109239243
          ],
          "min order - 75.0"
        ]
      }
    }
  }
]

clean_data(x)
# clean_data(null, "null31 CELINA ST", "The Peace Pipe")

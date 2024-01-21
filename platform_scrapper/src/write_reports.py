import os
import json
import pprint


def clean_data(list_of_circle_sections, store="aaa", address='bb', reporter=None):
    final_data = {}
    for item in list_of_circle_sections:
        if str(item)[0].isdigit():
            if type(list_of_circle_sections[item]) is list:
                final_data[item] = list_of_circle_sections[item]
        if type(item) is dict:
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
    filename = str(store) + str(address)
    if not reporter:
        with open(f"tmp__{filename}.json", 'w') as file:
            json.dump(res, file, indent=2)
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
    "3.0": {
      "0": {
        "0.5": [
          [
            46.505686474302166,
            -80.9446463
          ]
        ],
        "0.9": [
          [
            46.5137828190915,
            -80.9446463
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.52547751901767,
            -80.9446463
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.540770551908686,
            -80.9446463
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.55966188877184,
            -80.9446463
          ],
          "min order - 20.0"
        ]
      },
      "15": {
        "0.5": [
          [
            46.505533197177755,
            -80.94296028801665
          ]
        ],
        "0.9": [
          [
            46.51335362584138,
            -80.93992503115986
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.52464975573408,
            -80.93553986260564
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.53942155020175,
            -80.92980385649984
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.55766896618209,
            -80.92271582708591
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.57939195419411,
            -80.91427432759049
          ],
          "min order - 20.0"
        ]
      },
      "30": {
        "0.5": [
          [
            46.50508381384653,
            -80.94138920180183
          ]
        ],
        "0.9": [
          [
            46.51209530524896,
            -80.93552567114891
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.52222290323778,
            -80.92705455322688
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.53546653161789,
            -80.9159742448074
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.551826108930484,
            -80.90228269290311
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.57130154841507,
            -80.88597739304753
          ],
          "min order - 20.0"
        ],
        "2.9": [
          [
            46.59389275797145,
            -80.86705538719735
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.619599640121734,
            -80.8455132612544
          ],
          "min order - 20.0"
        ]
      },
      "45": {
        "0.5": [
          [
            46.50436895575847,
            -80.94004012792952
          ]
        ],
        "0.9": [
          [
            46.51009363804942,
            -80.9317481477599
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.51836242032369,
            -80.91976902632712
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.52917517244273,
            -80.90410091313177
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.542531760615915,
            -80.88474143909355
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.55843204733777,
            -80.861687714953
          ],
          "min order - 20.0"
        ],
        "2.9": [
          [
            46.57687589132512,
            -80.83493632931909
          ],
          "min order - 20.0"
        ]
      },
      "60": {
        "0.5": [
          [
            46.5034373484881,
            -80.9390050107414
          ]
        ],
        "0.9": [
          [
            46.50748507315941,
            -80.92884993635313
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.513331491942544,
            -80.91417992264917
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.52097642087142,
            -80.89499336795178
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.53041967401866,
            -80.87128822236909
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.54166106342888,
            -80.8430619868576
          ],
          "min order - 20.0"
        ],
        "2.9": [
          [
            46.55470039905199,
            -80.81031171206918
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.56953748867611,
            -80.77303399698123
          ],
          "min order - 20.0"
        ],
        "3.6999999999999997": [
          [
            46.58617213786063,
            -80.73122498730935
          ],
          "min order - 20.0"
        ]
      }
    },
    "10.0": {
      "0": {
        "2.5": [
          [
            46.58215149379478,
            -80.9446463
          ]
        ],
        "2.9": [
          [
            46.60823932434693,
            -80.9446463
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.637925330981254,
            -80.9446463
          ],
          "min order - 20.0"
        ]
      },
      "15": {
        "2.9": [
          [
            46.604590458327706,
            -80.90447764886544
          ]
        ],
        "3.3": [
          [
            46.63326441623359,
            -80.89332381778378
          ],
          "min order - 20.0"
        ]
      }
    }
  },
  {
    "3.0": {
      "72": {
        "0.5": [
          [
            46.50257828311761,
            -80.93845121567523
          ]
        ],
        "0.9": [
          [
            46.50507965025733,
            -80.9272995524116
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.50869238508712,
            -80.91119052712934
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.51341627048257,
            -80.89012305341619
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.51925108847727,
            -80.8640957412782
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.526196620213106,
            -80.83310689680087
          ],
          "min order - 20.0"
        ],
        "2.9": [
          [
            46.53425264589072,
            -80.79715452172032
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.54341894471965,
            -80.75623631290458
          ],
          "min order - 20.0"
        ],
        "3.6999999999999997": [
          [
            46.553695294868504,
            -80.71034966174453
          ],
          "min order - 20.0"
        ]
      },
      "87": {
        "0.5": [
          [
            46.501423720915014,
            -80.93814146762402
          ]
        ],
        "0.9": [
          [
            46.50184685218847,
            -80.92643267848271
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.50245765700581,
            -80.90951979358347
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.503255898507526,
            -80.88740262027693
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.504241339779966,
            -80.8600809123376
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.50541374384621,
            -80.82755437004177
          ],
          "min order - 20.0"
        ],
        "2.9": [
          [
            46.50677287365684,
            -80.78982264024297
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.50831849208082,
            -80.74688531644468
          ],
          "min order - 20.0"
        ]
      },
      "102": {
        "0.5": [
          [
            46.500253140666175,
            -80.93827501874955
          ]
        ],
        "0.9": [
          [
            46.4985692379859,
            -80.92680706650465
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.496136564259395,
            -80.91024298522656
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.49295489159228,
            -80.88858352665669
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.4890239919308,
            -80.86182965224876
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.484343637097155,
            -80.82998253305902
          ],
          "min order - 20.0"
        ],
        "2.9": [
          [
            46.478913598824725,
            -80.79304354959463
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.47273364879333,
            -80.75101429161997
          ],
          "min order - 20.0"
        ]
      },
      "117": {
        "0.5": [
          [
            46.499146313992696,
            -80.93884274032895
          ]
        ],
        "0.9": [
          [
            46.49547016537022,
            -80.92839703686353
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.490159862679704,
            -80.91331026697453
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.48321521324355,
            -80.89358392450227
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.474636023223184,
            -80.86921991915912
          ],
          "min order - 20.0"
        ]
      },
      "132": {
        "0.5": [
          [
            46.49817866332432,
            -80.93980592149335
          ]
        ],
        "0.9": [
          [
            46.49276080586869,
            -80.93109410540808
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.48493478983722,
            -80.91851217570114
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.47470047456508,
            -80.90206196764662
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.4620577165836,
            -80.881745826676
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.447006369685,
            -80.85756660689255
          ],
          "min order - 20.0"
        ]
      }
    }
  },
  {
    "3.0": {
      "144": {
        "0.5": [
          [
            46.49754949567748,
            -80.94081788030583
          ]
        ],
        "0.9": [
          [
            46.49099918981346,
            -80.93392755219878
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.481537490480314,
            -80.92397658151754
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.46916430142521,
            -80.91096672269366
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.453879522118925,
            -80.89490021738706
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.435683047804524,
            -80.87577979274594
          ],
          "min order - 20.0"
        ]
      },
      "159": {
        "0.5": [
          [
            46.49698925220873,
            -80.94231216722044
          ]
        ],
        "0.9": [
          [
            46.48943056410113,
            -80.9381113102654
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.478512391868485,
            -80.93204461958148
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.464234685815256,
            -80.92411332914178
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.446597390379566,
            -80.91431901532813
          ],
          "min order - 20.0"
        ]
      },
      "174": {
        "0.5": [
          [
            46.49671516052116,
            -80.94396548552741
          ]
        ],
        "0.9": [
          [
            46.48866313768614,
            -80.94274020032411
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.477032413722796,
            -80.94097072104593
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.46182296411548,
            -80.93865743105432
          ],
          "min order - 20.0"
        ]
      },
      "189": {
        "0.5": [
          [
            46.49674589519914,
            -80.94566518906132
          ]
        ],
        "0.9": [
          [
            46.48874919129045,
            -80.9474989205791
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.4771983675007,
            -80.95014708335883
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.4620933964122,
            -80.95360910760479
          ],
          "min order - 20.0"
        ]
      },
      "204": {
        "0.5": [
          [
            46.497079362222166,
            -80.94729547356802
          ]
        ],
        "0.9": [
          [
            46.489682862592005,
            -80.95206333955315
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.47899894909907,
            -80.9589489089871
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.46502756411428,
            -80.9679508113358
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.447768644416044,
            -80.97906729571282
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.37626596147555,
            -81.0250810615893
          ],
          "min order - 20.0"
        ]
      }
    },
    "10.0": {
      "204": {
        "2.5": [
          [
            46.427222121215976,
            -80.99229623242358
          ]
        ],
        "2.9": [
          [
            46.40338792018441,
            -81.0076351148381
          ],
          "min order - 20.0"
        ]
      }
    }
  },
  {
    "3.0": {
      "216": {
        "0.5": [
          [
            46.49754949567748,
            -80.94847471969418
          ]
        ],
        "0.9": [
          [
            46.49099918981346,
            -80.95536504780122
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.481537490480314,
            -80.96531601848247
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.46916430142521,
            -80.97832587730635
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.453879522118925,
            -80.99439238261294
          ],
          "min order - 20.0"
        ]
      },
      "231": {
        "0.5": [
          [
            46.49835771922546,
            -80.94970815716104
          ]
        ],
        "0.9": [
          [
            46.49326214905125,
            -80.95881864904831
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.48590164020881,
            -80.97197647342574
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.476276040918734,
            -80.98917982504558
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.46438519695768,
            -81.01042639671329
          ],
          "min order - 20.0"
        ]
      },
      "246": {
        "0.5": [
          [
            46.49935885323804,
            -80.95059668991358
          ]
        ],
        "0.9": [
          [
            46.49606526475527,
            -80.96130674510769
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.49130753405719,
            -80.9767754758497
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.485085459691625,
            -80.9970015097314
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.47739883930873,
            -81.0219830921446
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.46824746972089,
            -81.05171808690534
          ],
          "min order - 20.0"
        ]
      },
      "261": {
        "0.5": [
          [
            46.50048468055022,
            -80.9510797533093
          ]
        ],
        "0.9": [
          [
            46.4992175448121,
            -80.96265970027989
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.49738686089828,
            -80.97938572906648
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.494992396831464,
            -81.00125726833879
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.492033920571416,
            -81.02827358728153
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.48851120004215,
            -81.06043379561847
          ],
          "min order - 20.0"
        ],
        "4.1": [
          [
            46.46877323397698,
            -81.24049013961853
          ],
          "min order - 20.0"
        ],
        "4.5": [
          [
            46.4624258116047,
            -81.2983508643662
          ],
          "min order - 20.0"
        ],
        "4.9": [
          [
            46.4555127532719,
            -81.36134679255117
          ],
          "min order - 20.0"
        ]
      },
      "276": {
        "0.5": [
          [
            46.501658483065974,
            -80.95112440408491
          ]
        ],
        "0.9": [
          [
            46.50250418831556,
            -80.96278517227456
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.503725380726706,
            -80.97962888131381
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.505321825150766,
            -81.00165591496007
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.507293286294185,
            -81.02886676393301
          ],
          "min order - 20.0"
        ],
        "2.5": [
          [
            46.50963952870026,
            -81.06126202587494
          ],
          "min order - 20.0"
        ]
      }
    },
    "10.0": {
      "216": {
        "2.5": [
          [
            46.435683047804524,
            -81.01351280725406
          ]
        ],
        "2.9": [
          [
            46.41457476954564,
            -81.03568394070673
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.390554574274425,
            -81.06090209155728
          ],
          "min order - 20.0"
        ]
      },
      "231": {
        "2.5": [
          [
            46.45022895172516,
            -81.03571338065407
          ]
        ],
        "2.9": [
          [
            46.43380714631001,
            -81.06503747017973
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.41511961955653,
            -81.09839486165389
          ],
          "min order - 20.0"
        ],
        "3.6999999999999997": [
          [
            46.39416620813034,
            -81.13578125675383
          ],
          "min order - 20.0"
        ]
      },
      "246": {
        "2.9": [
          [
            46.457631146962655,
            -81.08620397702686
          ]
        ],
        "3.3": [
          [
            46.44554966635021,
            -81.1254378656403
          ],
          "min order - 20.0"
        ]
      },
      "261": {
        "2.9": [
          [
            46.484424003158956,
            -81.0977368436605
          ]
        ],
        "3.3": [
          [
            46.479772097855516,
            -81.1401815223779
          ],
          "min order - 20.0"
        ],
        "3.6999999999999997": [
          [
            46.47455525211098,
            -81.1877664634966
          ],
          "min order - 20.0"
        ]
      },
      "276": {
        "2.9": [
          [
            46.51236031673086,
            -81.09884240532163
          ]
        ],
        "3.3": [
          [
            46.51545541454814,
            -81.14160871368382
          ],
          "min order - 20.0"
        ],
        "3.6999999999999997": [
          [
            46.518924586096325,
            -81.18956186923911
          ],
          "min order - 20.0"
        ],
        "4.1": [
          [
            46.52276759508344,
            -81.24270289713446
          ],
          "min order - 20.0"
        ]
      }
    }
  },
  {
    "3.0": {
      "288": {
        "0.5": [
          [
            46.50257828311761,
            -80.95084138432478
          ]
        ],
        "0.9": [
          [
            46.50507965025733,
            -80.96199304758841
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.50869238508712,
            -80.97810207287067
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.51341627048257,
            -80.99916954658381
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.51925108847727,
            -81.0251968587218
          ],
          "min order - 20.0"
        ]
      },
      "303": {
        "0.5": [
          [
            46.50363814236538,
            -80.95010941997786
          ]
        ],
        "0.9": [
          [
            46.50804730805082,
            -80.95994383104373
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.51441582533532,
            -80.97415075080367
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.52274352028094,
            -80.99273186903585
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.53303021666484,
            -81.01568934853505
          ],
          "min order - 20.0"
        ]
      },
      "318": {
        "0.5": [
          [
            46.50453106362043,
            -80.94900510400763
          ]
        ],
        "0.9": [
          [
            46.510547553556805,
            -80.95685181691462
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.519237854875364,
            -80.96818776465092
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.53060184870697,
            -80.98301478775016
          ],
          "min order - 20.0"
        ]
      },
      "333": {
        "0.5": [
          [
            46.50519618639179,
            -80.94760368937091
          ]
        ],
        "0.9": [
          [
            46.51240995971082,
            -80.9529276945176
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.52282975875011,
            -80.96061939427305
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.53645551679427,
            -80.9706802864224
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.553287161587264,
            -80.98311228899816
          ],
          "min order - 20.0"
        ]
      },
      "348": {
        "0.5": [
          [
            46.50558817479176,
            -80.94600069011233
          ]
        ],
        "0.9": [
          [
            46.51350756929735,
            -80.94843894641107
          ],
          "min order - 20.0"
        ],
        "1.3": [
          [
            46.52494665854695,
            -80.95196161134878
          ],
          "min order - 20.0"
        ],
        "1.7000000000000002": [
          [
            46.53990541102265,
            -80.95656943810575
          ],
          "min order - 20.0"
        ],
        "2.1": [
          [
            46.55838378865166,
            -80.96226339130914
          ],
          "min order - 20.0"
        ]
      }
    },
    "10.0": {
      "288": {
        "2.5": [
          [
            46.526196620213106,
            -81.05618570319913
          ]
        ],
        "2.9": [
          [
            46.53425264589072,
            -81.09213807827969
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.54341894471965,
            -81.13305628709543
          ],
          "min order - 20.0"
        ],
        "3.6999999999999997": [
          [
            46.553695294868504,
            -81.17894293825547
          ],
          "min order - 20.0"
        ]
      },
      "303": {
        "2.5": [
          [
            46.54527573591111,
            -81.04302582620453
          ]
        ],
        "2.9": [
          [
            46.55947989702253,
            -81.07474441439615
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.575642516512225,
            -81.11084870249972
          ],
          "min order - 20.0"
        ],
        "3.6999999999999997": [
          [
            46.59376340833496,
            -81.1513427587831
          ],
          "min order - 20.0"
        ],
        "4.1": [
          [
            46.61384238381835,
            -81.1962311324847
          ],
          "min order - 20.0"
        ]
      },
      "318": {
        "2.1": [
          [
            46.54463941218811,
            -81.00133524265827
          ]
        ],
        "2.5": [
          [
            46.5613504184019,
            -81.0231520034107
          ],
          "min order - 20.0"
        ],
        "2.9": [
          [
            46.58073473631899,
            -81.04846846368049
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.602792230738345,
            -81.07728853919966
          ],
          "min order - 20.0"
        ]
      },
      "333": {
        "2.5": [
          [
            46.573324615300436,
            -80.99791774193635
          ]
        ],
        "2.9": [
          [
            46.596567794500395,
            -81.01509940909546
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.623016610117105,
            -81.03466048064162
          ],
          "min order - 20.0"
        ],
        "3.6999999999999997": [
          [
            46.652670967411936,
            -81.05660457580353
          ],
          "min order - 20.0"
        ]
      },
      "348": {
        "2.5": [
          [
            46.58038174679983,
            -80.96904464795148
          ]
        ],
        "2.9": [
          [
            46.60589923426534,
            -80.97691459851005
          ],
          "min order - 20.0"
        ],
        "3.3": [
          [
            46.634936193272665,
            -80.98587484826888
          ],
          "min order - 20.0"
        ],
        "3.6999999999999997": [
          [
            46.66749255946683,
            -80.99592721884572
          ],
          "min order - 20.0"
        ]
      }
    }
  }
]

# clean_data(x, reporter=False)
# clean_data(null, "null31 CELINA ST", "The Peace Pipe")


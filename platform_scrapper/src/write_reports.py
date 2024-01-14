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
            45.48191238370107,
            -76.6566934
          ]
        ],
        "0.9": [
          [
            45.49001018539515,
            -76.6566934
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.501706989708914,
            -76.6566934
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.51700277443679,
            -76.6566934
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.535897510541254,
            -76.6566934
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.55839116215334,
            -76.6566934
          ],
          "min order - 50.0"
        ]
      },
      "15": {
        "0.5": [
          [
            45.48175907943077,
            -76.65503819323074
          ]
        ],
        "0.9": [
          [
            45.489580916762215,
            -76.6520584087004
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.50087908227239,
            -76.6477534147344
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.515653539833316,
            -76.64212233429294
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.533904246900114,
            -76.6351640441552
          ],
          "min order - 50.0"
        ]
      },
      "30": {
        "0.5": [
          [
            45.481309616425094,
            -76.65349581149114
          ]
        ],
        "0.9": [
          [
            45.48832237479058,
            -76.64773943801107
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.49845180618521,
            -76.63942318561514
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.51169783646832,
            -76.62854553559687
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.52806038623289,
            -76.61510454322993
          ],
          "min order - 50.0"
        ]
      },
      "45": {
        "0.5": [
          [
            45.480594631326895,
            -76.65217138415733
          ]
        ],
        "0.9": [
          [
            45.48632035429695,
            -76.64403093107062
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.49459064649886,
            -76.63227077784126
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.505405381933436,
            -76.61688917151614
          ],
          "min order - 50.0"
        ]
      },
      "60": {
        "0.5": [
          [
            45.47966285804268,
            -76.65115517557145
          ]
        ],
        "0.9": [
          [
            45.48371132690162,
            -76.64118565759684
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.48955883072054,
            -76.62678375271582
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.497205191753004,
            -76.60794794366564
          ],
          "min order - 50.0"
        ]
      }
    }
  },
  {
    "0": {
      "72": {
        "0.5": [
          [
            45.47880363909054,
            -76.6506114948318
          ]
        ],
        "0.9": [
          [
            45.48130547541226,
            -76.63966358100187
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.48491890012981,
            -76.62384891669286
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            45.4896437036198,
            -76.60316647273791
          ],
          "min order - 50.0"
        ]
      },
      "87": {
        "0.5": [
          [
            45.47764886973024,
            -76.65030740088493
          ]
        ],
        "0.9": [
          [
            45.47807209816577,
            -76.63881251639835
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.47868305675458,
            -76.62220861486352
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            45.47948151690076,
            -76.6004955137661
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.48046724995552,
            -76.57367297982753
          ],
          "min order - 50.0"
        ],
        "2.9": [
          [
            45.48299961987835,
            -76.5046984269156
          ],
          "min order - 50.0"
        ]
      },
      "102": {
        "0.5": [
          [
            45.47647807857415,
            -76.65043850752951
          ]
        ],
        "0.9": [
          [
            45.47479389304311,
            -76.63918003643066
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.47236082362831,
            -76.62291850009797
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            45.4691786503523,
            -76.60165461064568
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.465247153072795,
            -76.57538927884255
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.46056611151669,
            -76.54412361400735
          ],
          "min order - 50.0"
        ],
        "2.9": [
          [
            45.45513530531406,
            -76.50785892386527
          ],
          "min order - 50.0"
        ]
      },
      "117": {
        "0.5": [
          [
            45.47537105166934,
            -76.65099585407576
          ]
        ],
        "0.9": [
          [
            45.47169425825831,
            -76.64074093825806
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.46638303487896,
            -76.62592967314377
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            45.459437195409755,
            -76.60656347385734
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.45085655255702,
            -76.58264414949066
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.44064091791632,
            -76.55417390237413
          ],
          "min order - 50.0"
        ]
      },
      "132": {
        "0.5": [
          [
            45.474403225301735,
            -76.65194143783327
          ]
        ],
        "0.9": [
          [
            45.46898440454377,
            -76.64338872556657
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.46115700448784,
            -76.63103651739691
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.450920889015364,
            -76.61488655190982
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.43827591919034,
            -76.59494105099394
          ],
          "min order - 50.0"
        ]
      }
    },
    "10.0": {
      "87": {
        "2.5": [
          [
            45.481640027208385,
            -76.54174072907612
          ]
        ]
      },
      "102": {
        "3.3": [
          [
            45.44895451403206,
            -76.4665967143651
          ]
        ],
        "3.6999999999999997": [
          [
            45.44202351720894,
            -76.42033868945724
          ],
          "min order - 50.0"
        ],
        "4.1": [
          [
            45.43434209438786,
            -76.36908675083262
          ],
          "min order - 50.0"
        ],
        "4.5": [
          [
            45.425910025150806,
            -76.31284299762254
          ],
          "min order - 50.0"
        ]
      },
      "132": {
        "2.5": [
          [
            45.423221953321956,
            -76.57120271845073
          ]
        ],
        "2.9": [
          [
            45.405758847027045,
            -76.54367473830106
          ],
          "min order - 50.0"
        ],
        "3.3": [
          [
            45.38588645329231,
            -76.51236077279009
          ],
          "min order - 50.0"
        ],
        "3.6999999999999997": [
          [
            45.363604622536215,
            -76.47726496009291
          ],
          "min order - 50.0"
        ],
        "4.1": [
          [
            45.338913202670575,
            -76.43839191172326
          ],
          "min order - 50.0"
        ]
      }
    }
  },
  {
    "0": {
      "144": {
        "0.5": [
          [
            45.47377394309195,
            -76.6529349102706
          ]
        ],
        "0.9": [
          [
            45.46722246578313,
            -76.6461704125045
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.45775907898783,
            -76.63640110584701
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.445383689283446,
            -76.6236286523101
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.430096198957926,
            -76.60785517549596
          ],
          "min order - 50.0"
        ]
      },
      "159": {
        "0.5": [
          [
            45.47321359739609,
            -76.65440190169534
          ]
        ],
        "0.9": [
          [
            45.46565355181029,
            -76.65027775612567
          ],
          "min order - 50.0"
        ],
        "1.3": [
          [
            45.45473342047593,
            -76.64432180682503
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.440453154728914,
            -76.63653522276942
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.42281270002788,
            -76.62691949733126
          ],
          "min order - 50.0"
        ]
      },
      "174": {
        "0.5": [
          [
            45.472939455621734,
            -76.65602502093506
          ]
        ],
        "0.9": [
          [
            45.464885984056465,
            -76.6548221099364
          ],
          "min order - 50.0"
        ],
        "1.3": [
          [
            45.4532531676003,
            -76.65308492908478
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.43804098179618,
            -76.65081384154972
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.41924939543546,
            -76.6480093112423
          ],
          "min order - 50.0"
        ]
      },
      "189": {
        "0.5": [
          [
            45.472970195918506,
            -76.65769367853699
          ]
        ],
        "0.9": [
          [
            45.46497205351972,
            -76.65949392527415
          ],
          "min order - 50.0"
        ],
        "1.3": [
          [
            45.453419152210856,
            -76.66209375067999
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.438311464744984,
            -76.66549261497049
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.41964895722485,
            -76.66968982862139
          ],
          "min order - 50.0"
        ]
      },
      "204": {
        "0.5": [
          [
            45.473303723865456,
            -76.65929418451464
          ]
        ],
        "0.9": [
          [
            45.4659058967229,
            -76.66397498426608
          ],
          "min order - 50.0"
        ],
        "1.3": [
          [
            45.45522006791069,
            -76.67073486238957
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.441246181137714,
            -76.67957252054225
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.42398417450895,
            -76.6904863000382
          ],
          "min order - 50.0"
        ]
      }
    },
    "10.0": {
      "144": {
        "2.5": [
          [
            45.411896506056955,
            -76.5890832589689
          ]
        ],
        "2.9": [
          [
            45.39078450443093,
            -76.56731594427815
          ],
          "min order - 50.0"
        ],
        "3.3": [
          [
            45.36676008378177,
            -76.54255672863373
          ],
          "min order - 50.0"
        ],
        "3.6999999999999997": [
          [
            45.33982312970934,
            -76.51480956223863
          ],
          "min order - 50.0"
        ]
      },
      "159": {
        "2.5": [
          [
            45.40181199597418,
            -76.61547644694909
          ]
        ],
        "2.9": [
          [
            45.37745097633171,
            -76.60220820951466
          ],
          "min order - 50.0"
        ]
      },
      "174": {
        "2.5": [
          [
            45.3968783705594,
            -76.64467190237397
          ]
        ],
        "2.9": [
          [
            45.370927862460555,
            -76.64080227892177
          ],
          "min order - 50.0"
        ],
        "3.3": [
          [
            45.341397819684104,
            -76.63640120400105
          ],
          "min order - 50.0"
        ],
        "3.6999999999999997": [
          [
            45.30828818402922,
            -76.6314695391467
          ],
          "min order - 50.0"
        ]
      }
    }
  },
  {
    "0": {
      "216": {
        "0.5": [
          [
            45.47377394309195,
            -76.66045188972939
          ]
        ],
        "0.9": [
          [
            45.46722246578313,
            -76.66721638749549
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.45775907898783,
            -76.67698569415298
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.445383689283446,
            -76.68975814768989
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.430096198957926,
            -76.70553162450403
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.411896506056955,
            -76.72430354103109
          ],
          "min order - 50.0"
        ]
      },
      "231": {
        "0.5": [
          [
            45.47458231376002,
            -76.66166279462908
          ]
        ],
        "0.9": [
          [
            45.46948583936866,
            -76.67060689880299
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.46212403254418,
            -76.68352447890248
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.45249674648287,
            -76.70041382478955
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.44060383192373,
            -76.72127275080427
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.42644513721295,
            -76.74609859704387
          ],
          "min order - 50.0"
        ],
        "2.9": [
          [
            45.410020508368284,
            -76.77488823092253
          ],
          "min order - 50.0"
        ]
      },
      "246": {
        "0.5": [
          [
            45.47558362942539,
            -76.66253509321739
          ]
        ],
        "0.9": [
          [
            45.47228946585308,
            -76.67304952843624
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.46753091569183,
            -76.6882357680813
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            45.46130778438454,
            -76.70809251206528
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.45361987646623,
            -76.73261809823501
          ],
          "min order - 50.0"
        ]
      },
      "261": {
        "0.5": [
          [
            45.47670966024542,
            -76.66300932784732
          ]
        ],
        "0.9": [
          [
            45.47544231704893,
            -76.6743777431642
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.47361134660113,
            -76.69079825581623
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            45.471216524999456,
            -76.71227032459535
          ],
          "min order - 50.0"
        ]
      },
      "276": {
        "0.5": [
          [
            45.477883674072956,
            -76.66305315814867
          ]
        ],
        "0.9": [
          [
            45.47872955235371,
            -76.67450089412655
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.479951008015846,
            -76.69103687010298
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            45.481547814108175,
            -76.7126614496284
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.485866569049215,
            -76.77117838017273
          ],
          "min order - 50.0"
        ]
      }
    },
    "10.0": {
      "216": {
        "2.9": [
          [
            45.39078450443093,
            -76.74607085572184
          ]
        ],
        "3.3": [
          [
            45.36676008378177,
            -76.77083007136626
          ],
          "min order - 50.0"
        ],
        "3.6999999999999997": [
          [
            45.33982312970934,
            -76.79857723776136
          ],
          "min order - 50.0"
        ]
      },
      "231": {
        "3.3": [
          [
            45.391329789143015,
            -76.80763804901059
          ]
        ],
        "3.6999999999999997": [
          [
            45.3703728210898,
            -76.84434397915129
          ],
          "min order - 50.0"
        ],
        "4.1": [
          [
            45.34714944362414,
            -76.88500148285274
          ],
          "min order - 50.0"
        ]
      },
      "246": {
        "2.5": [
          [
            45.44446699562184,
            -76.76181050295685
          ]
        ],
        "2.9": [
          [
            45.43384894474393,
            -76.79566734184085
          ],
          "min order - 50.0"
        ],
        "3.3": [
          [
            45.42176552599032,
            -76.83418587060348
          ],
          "min order - 50.0"
        ],
        "3.6999999999999997": [
          [
            45.408216540841494,
            -76.87736298606818
          ],
          "min order - 50.0"
        ],
        "4.1": [
          [
            45.39320179015791,
            -76.92519522730332
          ],
          "min order - 50.0"
        ],
        "4.5": [
          [
            45.37672107423705,
            -76.9776787768967
          ],
          "min order - 50.0"
        ]
      },
      "261": {
        "2.1": [
          [
            45.4682576282743,
            -76.73879325722164
          ]
        ],
        "2.5": [
          [
            45.464734432415185,
            -76.77036621036775
          ],
          "min order - 50.0"
        ],
        "2.9": [
          [
            45.46064671339684,
            -76.80698818970562
          ],
          "min order - 50.0"
        ],
        "3.3": [
          [
            45.455994247205304,
            -76.8486580499759
          ],
          "min order - 50.0"
        ],
        "3.6999999999999997": [
          [
            45.45077680986405,
            -76.89537449507974
          ],
          "min order - 50.0"
        ]
      },
      "276": {
        "2.1": [
          [
            45.48351974353714,
            -76.73937509758925
          ]
        ],
        "2.9": [
          [
            45.48858806321325,
            -76.80807196484153
          ],
          "min order - 50.0"
        ],
        "3.3": [
          [
            45.49168399840288,
            -76.85005662031833
          ],
          "min order - 50.0"
        ],
        "3.6999999999999997": [
          [
            45.49515414677892,
            -76.89713321658019
          ],
          "min order - 50.0"
        ],
        "4.1": [
          [
            45.49899828027179,
            -76.94930272486282
          ],
          "min order - 50.0"
        ],
        "4.5": [
          [
            45.50321617056391,
            -77.00656621767453
          ],
          "min order - 50.0"
        ]
      }
    }
  },
  {
    "0": {
      "288": {
        "0.5": [
          [
            45.47880363909054,
            -76.6627753051682
          ]
        ],
        "0.9": [
          [
            45.48130547541226,
            -76.67372321899812
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.48491890012981,
            -76.68953788330712
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            45.4896437036198,
            -76.71022032726208
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.49547967542297,
            -76.73577186761409
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.50242660419638,
            -76.76619410901709
          ],
          "min order - 50.0"
        ],
        "2.9": [
          [
            45.5104842776654,
            -76.80148894443045
          ],
          "min order - 50.0"
        ]
      },
      "303": {
        "0.5": [
          [
            45.479863687748946,
            -76.6620567095599
          ]
        ],
        "0.9": [
          [
            45.48427366167904,
            -76.67171141997257
          ],
          "min order - 50.0"
        ],
        "1.3": [
          [
            45.49064335589715,
            -76.68565868467452
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            45.49897260229745,
            -76.70390010438193
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.50926123049584,
            -76.72643772788163
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.5215090677642,
            -76.75327405305329
          ],
          "min order - 50.0"
        ],
        "2.9": [
          [
            45.53571593896438,
            -76.78441202812358
          ],
          "min order - 50.0"
        ]
      },
      "318": {
        "0.5": [
          [
            45.48075676801969,
            -76.66097256682686
          ]
        ],
        "0.9": [
          [
            45.486774350042715,
            -76.66867588718559
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.495466234838595,
            -76.67980461712078
          ],
          "min order - 0"
        ],
        "1.7000000000000002": [
          [
            45.506832307242,
            -76.69436050014244
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.520872448095744,
            -76.71234576845016
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.53758653419367,
            -76.73376314450222
          ],
          "min order - 50.0"
        ],
        "2.9": [
          [
            45.556974438223435,
            -76.75861584293109
          ],
          "min order - 50.0"
        ],
        "3.3": [
          [
            45.579036028709,
            -76.78690757280799
          ],
          "min order - 50.0"
        ]
      },
      "333": {
        "0.5": [
          [
            45.481422008905895,
            -76.65959675538258
          ]
        ],
        "0.9": [
          [
            45.48863708466203,
            -76.66482346223295
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.49905876775441,
            -76.67237454251872
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.512686993155675,
            -76.68225141506068
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.52952169029381,
            -76.69445589674419
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.549562783020825,
            -76.70899020406787
          ],
          "min order - 50.0"
        ],
        "2.9": [
          [
            45.572810189581325,
            -76.72585695503163
          ],
          "min order - 50.0"
        ],
        "3.3": [
          [
            45.599263822581115,
            -76.7450591713667
          ],
          "min order - 50.0"
        ],
        "3.6999999999999997": [
          [
            45.62892358895566,
            -76.76660028111128
          ],
          "min order - 50.0"
        ]
      },
      "348": {
        "0.5": [
          [
            45.48181406678322,
            -76.65802304393195
          ]
        ],
        "0.9": [
          [
            45.48973488726393,
            -76.66041673844391
          ],
          "min order - 0"
        ],
        "1.3": [
          [
            45.50117603680931,
            -76.66387499739469
          ],
          "min order - 50.0"
        ],
        "1.7000000000000002": [
          [
            45.516137484229056,
            -76.66839853425387
          ],
          "min order - 50.0"
        ],
        "2.1": [
          [
            45.53461919176841,
            -76.67398826277437
          ],
          "min order - 50.0"
        ],
        "2.5": [
          [
            45.55662111510137,
            -76.68064529785129
          ],
          "min order - 50.0"
        ],
        "2.9": [
          [
            45.58214320332386,
            -76.68837095656842
          ],
          "min order - 50.0"
        ]
      }
    },
    "10.0": {
      "288": {
        "3.3": [
          [
            45.51965248257581,
            -76.84165855560582
          ]
        ],
        "3.6999999999999997": [
          [
            45.52993100464569,
            -76.88670541365832
          ],
          "min order - 50.0"
        ],
        "4.1": [
          [
            45.54131962851724,
            -76.93663227972232
          ],
          "min order - 50.0"
        ],
        "4.5": [
          [
            45.55381813770859,
            -76.9914422056921
          ],
          "min order - 50.0"
        ],
        "4.9": [
          [
            45.567426314565324,
            -77.05113853504776
          ],
          "min order - 50.0"
        ]
      },
      "303": {
        "3.3": [
          [
            45.5518816664823,
            -76.81985505315359
          ]
        ],
        "3.6999999999999997": [
          [
            45.57000607016154,
            -76.85960698176042
          ],
          "min order - 50.0"
        ],
        "4.1": [
          [
            45.59008896723691,
            -76.90367212307477
          ],
          "min order - 50.0"
        ],
        "4.5": [
          [
            45.612130172267555,
            -76.952055243936
          ],
          "min order - 50.0"
        ],
        "4.9": [
          [
            45.63612949706998,
            -77.0047615713266
          ],
          "min order - 50.0"
        ]
      }
    }
  }
]

clean_data(x)
# clean_data(null, "null31 CELINA ST", "The Peace Pipe")

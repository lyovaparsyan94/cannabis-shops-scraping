import pprint
delivery_area = {2.99: {'degree': {1.4: [1213154546]}}, 'minimum_order': 0}
delivery_area_example = {'price': {'degree': {'km': ['coordinates',1213154546]}}, 'minimum_order': 0}
y = {1: {10: {0: []}},
 14.99: {0: {0.5: [(22.92348294095433, -22.0211127)]}},
 'minimum_order': 100.0}

z = {0.99: {88: {12: []}},
 12.99: {50: {1.5: [(43.92348294095433, -79.0211127)]}},
 'minimum_order': 100.0}

pprint.pprint(z | y)
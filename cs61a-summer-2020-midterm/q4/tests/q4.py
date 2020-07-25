test = {
  'name': 'q4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> subbasket(2233) # 22 counts
          True
          
          >>> subbasket(2444423) # 4444 counts
          True
          
          >>> subbasket(82223) # 22 counts even if it appears as part of 222
          True
          
          >>> subbasket(234562) # 2...2 does not count if the 2s are not consecutive
          False
          
          >>> subbasket(1) # 1 counts
          True
          
          >>> subbasket(498729879871) # 1 counts
          True
          
          >>> subbasket(149872987987) # 1 counts
          True
          
          >>> subbasket(4445555) # no baskets in this number
          False
          
          >>> subbasket(20) # no baskets in this number
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q4 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

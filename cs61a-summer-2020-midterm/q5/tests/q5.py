test = {
  'name': 'q5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> elevator(['a', 'b', 'c'], [1, 2, 3])
          ['a', 'b', 'b', 'c', 'c', 'c']
          
          >>> elevator(['a', 'b', 'c'], [3])
          ['a', 'a', 'a']
          
          >>> elevator(['a', 'b', 'c'], [0, 2, 0])
          ['b', 'b']
          
          >>> elevator([], [1,2,3])
          []
          
          >>> elevator(['a', 'b', 'c'], [1, -1, 3])
          ['c', 'c', 'c']
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q5 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

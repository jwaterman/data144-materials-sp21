test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Did you name your column correctly?
          >>> 'errors' in CEdata.labels
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # is errors an array?
          >>> isinstance(errors, (np.ndarray))
          True
          """,
          'hidden': False,
          'locked': False
        },          
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

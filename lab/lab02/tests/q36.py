test = {
  'name': 'q36',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pok_markets.num_rows == 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(pok_markets.column('city')) == ['Poughkeepsie', 'Poughkeepsie', 'Poughkeepsie']
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

test = {
  'name': 'q3_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(change_in_death_rates, Table)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> change_in_death_rates.num_rows
          88
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(change_in_death_rates.group('Year', np.average).column("Murder Rate average"), np.array([7.51363638, 8.12045454]))
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

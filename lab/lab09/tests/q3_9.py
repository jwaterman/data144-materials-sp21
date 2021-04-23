test = {
  'name': 'q3_9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(find_test_stat(change_in_death_rates, "Murder Rate", "Death Penalty"), 3) - 0.607 <= 0.01
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

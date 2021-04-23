test = {
  'name': 'q3_10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.random.seed(123);
          >>> round(simulate_and_test_statistic(change_in_death_rates, "Murder Rate", "Death Penalty"), 3)
          -1.398
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

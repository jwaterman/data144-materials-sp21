test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> correct_order = make_array(5, 1, 3, 2, 4, 6);
          >>> correct = 0;
          >>> for i in np.arange(6):
          ...     if ab_test_order.item(i) == correct_order.item(i):
          ...         correct = correct + 1;
          >>> correct == 6
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

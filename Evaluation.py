import graphlab


def compare_models(test_data, m1, m2):
    model_performance = graphlab.compare(test_data, [m1, m2])
    graphlab.show_comparison(model_performance, [m1, m2])

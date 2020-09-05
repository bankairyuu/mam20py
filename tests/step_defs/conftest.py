"""
This module contains shared fixtures, steps, and hooks.
"""


def pytest_bdd_step_error(request, feature, scenario, step, step_func_step_func_args, exception):
    print(f'step failed: {step}')

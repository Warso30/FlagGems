import logging

import triton

from ..utils.pointwise_dynamic import pointwise_dynamic


@pointwise_dynamic(promotion_methods=[(0, 1, "DEFAULT")])
@triton.jit
def bitwise_or_func(x, y):
    return x | y


def bitwise_or_tensor(A, B):
    logging.debug("GEMS_CAMBRICON BITWISE OR")
    return bitwise_or_func(A, B)


@pointwise_dynamic(is_tensor=[True, False], promotion_methods=[(0, 1, "DEFAULT")])
@triton.jit
def bitwise_or_func_scalar(x, y):
    return x | y


def bitwise_or_scalar(A, B):
    logging.debug("GEMS_CAMBRICON BITWISE OR SCALAR")
    return bitwise_or_func_scalar(A, B)


def bitwise_or_scalar_tensor(A, B):
    logging.debug("GEMS_CAMBRICON BITWISE OR SCALAR TENSOR")
    return bitwise_or_func_scalar(B, A)

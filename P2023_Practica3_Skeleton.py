#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from decimal import Decimal

P_INFINITY = (None, None)


# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed


# ----------------------------------------------------------------------------


def uoc_ComputePoints(curve):
    """
    EXERCISE 1.1: Count the points on an elliptic curve
    :curve: a list with the curve values [a, b, p]
    :return: number of points on the curve
    """

    num_points = 0

    #### IMPLEMENTATION GOES HERE ####
    a, b, p = (curve[0], curve[1], curve[2])
    print(f'a = {a}, b = {b}, p = {p}')

    if 4 * pow(a, 3) + 27 * pow(b, 2) == 0 or p <= 3:
        raise Exception("parameters are incorrect.")

    points = [P_INFINITY]
    for x in range(p):
        for y in range(p):
            x_val = (pow(x, 3) + a * x + b)
            y_val = pow(y, 2)
            if (y_val - x_val) % p == 0:
                points.append((x, y))

    num_points = len(points)
    print(f'size = {num_points}, points = {points}')
    # --------------------------------

    return num_points


def uoc_VerifyNumPoints(curve, n):
    """
    EXERCISE 1.2: Verify group order
    :curve: a list with the curve values [a, b, p]
    :n: number of points
    :return: True if it satisfies the equation or False
    """

    result = False

    #### IMPLEMENTATION GOES HERE ####
    p = curve[2]

    if n < 0:
        return False

    # we use Decimal to avoid wrong evaluations like 0.1 + 0.2 != 0.3
    below = Decimal(p + 1 - 2 * math.sqrt(p))
    above = Decimal(p + 1 + 2 * math.sqrt(p))

    result = below <= Decimal(n) <= above
    # --------------------------------

    return result


def uoc_AddPoints(curve, P, Q):
    """
    EXERCISE 2.1: Add two points
    :curve: a list with the curve values [a, b, p]
    :P: a point as a pair (x, y)
    :Q: another point as a pair (x, y)
    :return: P+Q
    """

    # R = P+Q
    suma = None

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------
    return suma


def uoc_SelfProductPoint(curve, n, P):
    """
    EXERCISE 3.1: Multiplication of a scalar by a point
    :curve: a list with the curve values [a, b, p]
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    # R = nP
    product = None

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------
    return product


def uoc_IsGroup(curve):
    """
    EXERCISE 3.2: xxx
    :curve: check if the curve is a group
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    result = None

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------
    return result


def uoc_OrderPoint(curve, P):
    """
    EXERCISE 3.3: Point order
    :curve: a list with the curve values [a, b, p]
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    point_order = None

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------
    return point_order


def uoc_GenKey(curve, P):
    """
    EXERCISE 4.1: Generate a pair of keys
    :curve: a list with the curve values [a, b, p]
    :P: a point as a pair (x, y)
    :return: a pair of keys (pub, priv)
    """

    key = (None, None)

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------
    return key


def uoc_SharedKey(curve, priv_user1, pub_user2):
    """
    EXERCISE 4.2: Generate a shared secret
    :curve: a list with the curve values [a, b, p]
    :pub_user1: a public key
    :pub_user2: a private key
    :return: shared secret
    """

    shared = None

    #### IMPLEMENTATION GOES HERE ####

    # --------------------------------
    return shared

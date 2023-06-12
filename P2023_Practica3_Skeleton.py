#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import random
from decimal import Decimal
from fractions import Fraction

P_INFINITY = (None, None)


# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
def mod(x, p):
    return x % p


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

    # validate the input
    if 4 * pow(a, 3) + 27 * pow(b, 2) == 0 or p <= 3:
        raise Exception("parameters are incorrect.")

    points = [P_INFINITY]
    # for all possible x values
    for x in range(p):
        # we then evaluate y values
        for y in range(p):
            # we calculate right side of equation (x^3 + ax + b)
            x_val = (pow(x, 3) + a * x + b)
            # we calculate left side of equation (y^2)
            y_val = pow(y, 2)
            # if differences are divisible by p, we add it to the list of points
            if mod(y_val - x_val, p) == 0:
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

    # we verify n is not below 0
    if n < 0:
        return False

    # we use Decimal to avoid wrong evaluations like 0.1 + 0.2 != 0.3
    below = Decimal(p + 1 - 2 * math.sqrt(p))
    above = Decimal(p + 1 + 2 * math.sqrt(p))

    # number of points is between 1+2-2sqrt(p) <= result <= 1+2+2sqrt(p)
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
    x1, y1 = (P[0], P[1])
    x2, y2 = (Q[0], Q[1])
    a, b, p = (curve[0], curve[1], curve[2])

    if P == P_INFINITY:  # 0Q = Q
        return Q
    if Q == P_INFINITY:  # P0 = P
        return P

    # Rules for the sum of eliptic curve points
    if x1 != x2:  # 1. use curve slope
        sc = mod((y1 - y2) * pow(x1 - x2, -1, p), p)
        x3 = mod(pow(sc, 2, p) - x1 - x2, p)
        y3 = mod(sc * (x1 - x3) - y1, p)
        suma = (x3, y3)
    else:
        if y1 == y2 and y1 != 0:  # 2. use tangent method (P=Q)
            st = mod((3 * pow(x1, 2, p) + a) * pow(2 * y1, -1, p), p)
            x3 = mod(pow(st, 2, p) - 2 * x1, p)
            y3 = mod(st * (x1 - x3) - y1, p)
            suma = (x3, y3)
        elif y1 == -y2 or y1 != y2:  # 3. PQ = 0
            suma = P_INFINITY

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
    # we'll use double and add method to also handle big scalar numbers

    # first, calculate the binary expansion of scalar n and reverse it
    binary_reversed = (bin(n)[2:])[::-1]

    p_tmp = P
    q = P_INFINITY
    # iterate over each element of the binary reversed
    for i in range(len(binary_reversed)):
        # only if value is 1 we do the add
        if binary_reversed[i] == "1":
            q = uoc_AddPoints(curve, p_tmp, q)
        # we double each time
        p_tmp = uoc_AddPoints(curve, p_tmp, p_tmp)

    product = q
    # --------------------------------
    return product


def uoc_IsGroup(curve):
    """
    EXERCISE 3.2: xxx
    :curve: check if the curve is a group
    :return: true if is group, false otherwise
    """

    result = None

    #### IMPLEMENTATION GOES HERE ####
    a, b, p = (curve[0], curve[1], curve[2])

    # as defined in ex1, a,b need to satisfy 4a^3 +27b^2 != 0
    result = mod(4 * pow(a, 3) + 27 * pow(b, 2), p) != 0
    print(f'is group? {result}')
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
    keep_loop = True
    point_order = 0

    # order is equal to the number of iterations we need to find P_INFINITY (first scalar that nP = 0)
    while keep_loop:
        point_order += 1
        # we calculate each nP
        result = uoc_SelfProductPoint(curve, point_order, P)
        # check if current nP is infinity.
        #  - true we stop and point_order is the order
        #  - false we keep looping
        keep_loop = result != P_INFINITY

    print(f'order = {point_order}')
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
    p = curve[2]
    # generate private key that is a random number [1,p)
    private_key = random.randint(1, p - 1)
    # calculate public key, privKey * P
    public_key = uoc_SelfProductPoint(curve, private_key, P)
    key = (public_key, private_key)
    # --------------------------------
    return key


def uoc_SharedKey(curve, priv_user1, pub_user2):
    """
    EXERCISE 4.2: Generate a shared secret
    :curve: a list with the curve values [a, b, p]
    :pub_user1: a private key
    :pub_user2: a public key
    :return: shared secret
    """

    shared = None

    #### IMPLEMENTATION GOES HERE ####
    # private key acts like scalar n and public key acts like the point P
    shared = uoc_SelfProductPoint(curve, priv_user1, pub_user2)
    # --------------------------------
    return shared

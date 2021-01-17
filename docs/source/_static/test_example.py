#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2021 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#

#  This file is part of Pynguin.
#
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#

# Automatically generated by Pynguin.
import example as module0


def test_case_0():
    var0 = -2603
    var1 = module0.triangle(var0, var0, var0)
    assert var1 == "Equilateral triangle"


def test_case_1():
    var0 = -2603
    var1 = module0.triangle(var0, var0, var0)
    assert var1 == "Equilateral triangle"
    var2 = 1272
    var3 = module0.triangle(var0, var2, var2)
    assert var3 == "Isosceles triangle"


def test_case_2():
    var0 = -32
    var1 = None
    var2 = module0.triangle(var0, var1, var0)
    assert var2 == "Isosceles triangle"


def test_case_3():
    var0 = -32
    var1 = None
    var2 = module0.triangle(var0, var1, var0)
    assert var2 == "Isosceles triangle"
    var3 = -2603
    var4 = module0.triangle(var3, var3, var3)
    assert var4 == "Equilateral triangle"
    var5 = 1272
    var6 = module0.triangle(var3, var5, var5)
    assert var6 == "Isosceles triangle"
    var7 = -38
    var8 = module0.triangle(var5, var7, var3)
    assert var8 == "Scalene triangle"


def test_case_4():
    var0 = -32
    var1 = None
    var2 = module0.triangle(var0, var1, var0)
    assert var2 == "Isosceles triangle"
    var3 = -2603
    var4 = module0.triangle(var3, var3, var3)
    assert var4 == "Equilateral triangle"
    var5 = 1272
    var6 = module0.triangle(var3, var5, var5)
    assert var6 == "Isosceles triangle"
    var7 = -38
    var8 = module0.triangle(var5, var7, var3)
    assert var8 == "Scalene triangle"
    var9 = -4217
    var10 = module0.triangle(var9, var1, var1)
    assert var10 == "Isosceles triangle"


def test_case_5():
    var0 = -32
    var1 = None
    var2 = module0.triangle(var0, var1, var0)
    assert var2 == "Isosceles triangle"
    var3 = -2603
    var4 = module0.triangle(var3, var3, var3)
    assert var4 == "Equilateral triangle"
    var5 = 1272
    var6 = module0.triangle(var3, var5, var5)
    assert var6 == "Isosceles triangle"
    var7 = module0.triangle(var0, var0, var1)
    assert var7 == "Isosceles triangle"

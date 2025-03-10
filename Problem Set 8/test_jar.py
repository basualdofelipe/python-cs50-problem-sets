from jar import Jar
import pytest

def test_jar_str():
    jar = Jar(20)
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.withdraw(4)
    assert str(jar) == ""

def test_jar_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    jar.deposit(2)
    assert jar.size == 12

def test_jar_withdraw():
    jar = Jar(20)
    jar.deposit(20)
    jar.withdraw(10)
    assert jar.size == 10
    jar.withdraw(2)
    assert jar.size == 8

def test_jar_exceed():
    jar = Jar(50)
    with pytest.raises(ValueError, match="Can't exceed the jar capacity"):
        jar.deposit(55)
    with pytest.raises(ValueError, match="Can't exceed the jar capacity"):
        jar.deposit(51)
    jar.deposit(50)
    assert jar.size == 50
 
def test_jar_negative_cookies():
    jar = Jar()
    with pytest.raises(ValueError, match=f"Can't withdraw more than {jar.size} size"):
        jar.withdraw(1)
    jar.deposit(8)
    with pytest.raises(ValueError, match=f"Can't withdraw more than {jar.size} size"):
        jar.withdraw(10)

def test_jar_negative_capacity():
    with pytest.raises(ValueError, match="Capacity can't be negative"):
        jar = Jar(-10)
    with pytest.raises(ValueError, match="Capacity can't be negative"):
        jar = Jar(-18)
    
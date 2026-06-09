def input_temperature(temp_str: str) -> int:
    num1 = int(temp_str)
    if (num1 > 40):
        raise ValueError(f"{num1}°C is too hot for plants (max 40°C)")
    elif (num1 < 0):
        raise ValueError(f"{num1}°C is too cold for plants (min 0°C)")
    return (num1)


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        num1 = input_temperature('25')
        print(f"Temperature is now {num1}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("\nInput data is 'abc'")
    try:
        num1 = input_temperature('abc')
        print(f"Temperature is now {num1}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("\nInput data is '100'")
    try:
        num1 = input_temperature('100')
        print(f"Temperature is now {num1}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("\nInput data is '-50'")
    try:
        num1 = input_temperature('-50')
        print(f"Temperature is now {num1}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()

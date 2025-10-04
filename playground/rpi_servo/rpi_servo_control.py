#!/usr/bin/env python3
"""
Servo Motor Diagnostic Tool for Raspberry Pi 5
Helps identify wiring and configuration issues
"""

from gpiozero import Servo, OutputDevice
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep
import sys


def test_gpio_output(*, gpio_pin: int = 18) -> bool:
    """
    Test if the GPIO pin can output signals at all.
    
    Args:
        gpio_pin: The GPIO pin to test
        
    Returns:
        True if test passed, False otherwise
    """
    print(f"\n{'='*60}")
    print("TEST 1: Basic GPIO Output Test")
    print(f"{'='*60}")
    print(f"Testing if GPIO {gpio_pin} can output signals...")
    
    try:
        factory = LGPIOFactory()
        led = OutputDevice(pin=gpio_pin, pin_factory=factory)
        
        print("Toggling GPIO pin 5 times (if you have an LED/multimeter, you should see it)...")
        for i in range(5):
            led.on()
            print(f"  {i+1}. Pin HIGH")
            sleep(0.5)
            led.off()
            print(f"     Pin LOW")
            sleep(0.5)
        
        led.close()
        print("✓ GPIO pin is working!\n")
        return True
        
    except Exception as e:
        print(f"✗ GPIO test failed: {e}\n")
        return False


def test_servo_extreme_positions(*, gpio_pin: int = 18) -> None:
    """
    Test servo with very obvious extreme positions.
    
    Args:
        gpio_pin: The GPIO pin connected to servo
    """
    print(f"{'='*60}")
    print("TEST 2: Servo Extreme Position Test")
    print(f"{'='*60}")
    print("Watch your servo carefully - it should move noticeably!\n")
    
    try:
        factory = LGPIOFactory()
        
        # Try different pulse width ranges in case servo needs calibration
        test_configs = [
            ("Standard (1ms-2ms)", 1.0/1000, 2.0/1000),
            ("Extended (0.5ms-2.5ms)", 0.5/1000, 2.5/1000),
            ("Narrow (1.2ms-1.8ms)", 1.2/1000, 1.8/1000),
        ]
        
        for name, min_pw, max_pw in test_configs:
            print(f"\nTrying {name} pulse width range...")
            print(f"Min: {min_pw*1000:.2f}ms, Max: {max_pw*1000:.2f}ms")
            
            servo = Servo(
                pin=gpio_pin,
                min_pulse_width=min_pw,
                max_pulse_width=max_pw,
                pin_factory=factory
            )
            
            print("  → Moving to MINIMUM position...")
            servo.min()
            sleep(2)
            
            print("  → Moving to MAXIMUM position...")
            servo.max()
            sleep(2)
            
            print("  → Moving to CENTER position...")
            servo.mid()
            sleep(2)
            
            servo.close()
            
            response = input("Did the servo move? (y/n): ").strip().lower()
            if response == 'y':
                print(f"✓ Success! Use these pulse widths: min={min_pw*1000:.2f}ms, max={max_pw*1000:.2f}ms\n")
                return
            else:
                print("✗ No movement detected, trying next configuration...\n")
        
        print("✗ Servo didn't move with any configuration.\n")
        
    except Exception as e:
        print(f"✗ Servo test failed: {e}\n")


def test_manual_pwm_values(*, gpio_pin: int = 18) -> None:
    """
    Test servo with manual PWM value control for maximum visibility.
    
    Args:
        gpio_pin: The GPIO pin connected to servo
    """
    print(f"{'='*60}")
    print("TEST 3: Manual PWM Value Test")
    print(f"{'='*60}")
    print("Testing with explicit PWM values...\n")
    
    try:
        factory = LGPIOFactory()
        servo = Servo(
            pin=gpio_pin,
            min_pulse_width=1.0/1000,
            max_pulse_width=2.0/1000,
            pin_factory=factory
        )
        
        test_values = [
            (-1.0, "Full CCW/Minimum (0°)"),
            (-0.5, "Quarter position (45°)"),
            (0.0, "Center (90°)"),
            (0.5, "Three-quarter position (135°)"),
            (1.0, "Full CW/Maximum (180°)"),
            (0.0, "Back to center (90°)"),
        ]
        
        for value, description in test_values:
            print(f"Setting servo.value = {value:+.1f} [{description}]")
            servo.value = value
            sleep(3)  # Long delay to see movement clearly
        
        servo.close()
        print("\n✓ Manual PWM test complete.\n")
        
    except Exception as e:
        print(f"✗ Manual PWM test failed: {e}\n")


def check_wiring() -> None:
    """Display wiring instructions and checklist."""
    print(f"\n{'='*60}")
    print("WIRING CHECKLIST")
    print(f"{'='*60}")
    print("""
Your servo should be wired like this:

Servo Wire    →  Connect To
----------       ----------
BROWN (GND)   →  Breadboard ground rail  →  Pi Pin 6 (or any GND)
RED (5V)      →  Breadboard 5V rail      →  Pi Pin 2 or 4 (5V)
YELLOW (PWM)  →  Breadboard row          →  Pi Pin 12 (GPIO 18)

CRITICAL CHECKS:
☐ Is the RED wire connected to 5V rail (NOT to GPIO pin)?
☐ Is the BROWN wire connected to GND rail?
☐ Is the YELLOW wire connected to GPIO 18 (physical pin 12)?
☐ Are the power rails on breadboard connected to Pi 5V and GND?
☐ Is your Pi power supply at least 2.5A (3A recommended)?
☐ Are the connections physically secure (no loose wires)?

NOTE: If servo still doesn't move, it might be:
1. Faulty servo (try a different one)
2. Insufficient power supply (try a 5A power adapter)
3. Wrong GPIO pin (try GPIO 17, pin 11 instead)
""")
    
    input("\nPress Enter when you've checked all wiring...")


def main() -> None:
    """Run all diagnostic tests."""
    print("\n" + "="*60)
    print("RASPBERRY PI 5 SERVO DIAGNOSTIC TOOL")
    print("="*60)
    print("\nThis tool will help identify why your servo isn't moving.\n")
    
    # Check wiring first
    check_wiring()
    
    # Get GPIO pin
    gpio_input = input("\nWhich GPIO pin is your servo connected to? [18]: ").strip()
    gpio_pin = int(gpio_input) if gpio_input else 18
    
    print(f"\nUsing GPIO pin: {gpio_pin}")
    print(f"Physical pin location: Pin {(gpio_pin * 2) if gpio_pin < 14 else 'varies'}")
    print("\nStarting diagnostic tests...\n")
    sleep(1)
    
    # Run tests
    test_gpio_output(gpio_pin=gpio_pin)
    sleep(1)
    
    test_servo_extreme_positions(gpio_pin=gpio_pin)
    sleep(1)
    
    test_manual_pwm_values(gpio_pin=gpio_pin)
    
    # Final recommendations
    print(f"{'='*60}")
    print("DIAGNOSTIC COMPLETE")
    print(f"{'='*60}")
    print("""
If your servo STILL didn't move:

1. POWER ISSUE (Most Common):
   - Try a more powerful Pi power supply (5A USB-C recommended)
   - Try using an external 5V power supply for the servo
   - Check if power rails on breadboard are actually connected
   
2. WIRING ISSUE:
   - Use a multimeter to verify 5V on red wire
   - Use a multimeter to verify GND on brown wire
   - Try a different breadboard row for the signal wire
   
3. SERVO ISSUE:
   - Try a different servo to rule out defective unit
   - Some servos need 6V instead of 5V
   
4. SOFTWARE ISSUE:
   - Try a different GPIO pin (e.g., GPIO 17, pin 11)
   - Update gpiozero: pip install --upgrade gpiozero
   - Check if lgpio is installed: pip install lgpio

Need more help? Run: 'pinout' command to see Pi's pin layout
""")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDiagnostic interrupted by user. Goodbye!")
        sys.exit(0)
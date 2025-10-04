#!/usr/bin/env python3
"""
Servo Motor Control for Raspberry Pi 5
Educational example showing basic servo control using PWM
"""

from gpiozero import Servo
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep


def setup_servo(*, gpio_pin: int = 18) -> Servo:
    """
    Initialize the servo motor on the specified GPIO pin.
    
    Args:
        gpio_pin: The GPIO pin number (BCM numbering) connected to servo signal wire
        
    Returns:
        Configured Servo object
        
    Note:
        - min_pulse_width: minimum pulse width in seconds (1ms = -1 or 0°)
        - max_pulse_width: maximum pulse width in seconds (2ms = +1 or 180°)
        These values may need tuning for your specific servo!
    """
    # Use LGPIOFactory for Raspberry Pi 5 compatibility
    factory = LGPIOFactory()
    
    servo = Servo(
        pin=gpio_pin,
        min_pulse_width=1.0/1000,  # 1ms
        max_pulse_width=2.0/1000,  # 2ms
        pin_factory=factory
    )
    
    return servo


def move_to_angle(*, servo: Servo, angle: float) -> None:
    """
    Move servo to a specific angle.
    
    Args:
        servo: The Servo object to control
        angle: Target angle in degrees (0 to 180)
        
    Note:
        gpiozero uses values from -1 to +1:
        -1 = minimum (0°)
         0 = middle (90°)
        +1 = maximum (180°)
    """
    # Convert angle (0-180) to gpiozero value (-1 to +1)
    if not 0 <= angle <= 180:
        raise ValueError("Angle must be between 0 and 180 degrees")
    
    value = (angle / 90.0) - 1.0
    servo.value = value
    print(f"Moved to {angle}° (value: {value:.2f})")


def sweep_servo(*, servo: Servo, delay: float = 0.5) -> None:
    """
    Sweep the servo back and forth through its full range.
    
    Args:
        servo: The Servo object to control
        delay: Delay in seconds between positions
    """
    print("\nSweeping servo through full range...")
    
    # Method 1: Using angle conversion
    for angle in [0, 45, 90, 135, 180, 135, 90, 45, 0]:
        move_to_angle(servo=servo, angle=angle)
        sleep(delay)
    
    print("\nUsing built-in methods...")
    
    # Method 2: Using built-in methods
    servo.min()      # 0° position
    print("Position: min (0°)")
    sleep(delay)
    
    servo.mid()      # 90° position
    print("Position: mid (90°)")
    sleep(delay)
    
    servo.max()      # 180° position
    print("Position: max (180°)")
    sleep(delay)
    
    servo.mid()      # Return to center
    print("Position: mid (90°)")


def interactive_control(*, servo: Servo) -> None:
    """
    Interactive control allowing user to specify angles.
    
    Args:
        servo: The Servo object to control
    """
    print("\n" + "="*50)
    print("Interactive Servo Control")
    print("="*50)
    print("Enter angles from 0 to 180 degrees")
    print("Enter 'q' to quit")
    print("Enter 's' for sweep demo")
    print("="*50 + "\n")
    
    while True:
        user_input = input("Enter angle or command: ").strip().lower()
        
        if user_input == 'q':
            print("Exiting...")
            break
        elif user_input == 's':
            sweep_servo(servo=servo, delay=0.3)
        else:
            try:
                angle = float(user_input)
                move_to_angle(servo=servo, angle=angle)
                sleep(0.5)  # Give servo time to reach position
            except ValueError:
                print("Invalid input! Enter a number (0-180), 's' for sweep, or 'q' to quit")


def main() -> None:
    """Main function to run the servo control program."""
    print("Raspberry Pi 5 Servo Control")
    print("============================\n")
    
    # Initialize servo on GPIO 18
    servo = setup_servo(gpio_pin=18)
    
    try:
        # Center the servo on startup
        print("Centering servo...")
        servo.mid()
        sleep(1)
        
        # Run demo sweep
        sweep_servo(servo=servo, delay=0.5)
        
        # Enter interactive mode
        interactive_control(servo=servo)
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")
    
    finally:
        # Clean shutdown - return to center and detach
        print("Returning to center position...")
        servo.mid()
        sleep(0.5)
        servo.value = None  # Stop sending pulses
        servo.close()
        print("Servo control released. Goodbye!")


if __name__ == "__main__":
    main()
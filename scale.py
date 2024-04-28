def scale_value(val, old_min, old_max, new_min, new_max):
  """
  Scales a value from one range to another while keeping it as an integer.

  Args:
      val: The value to scale (between old_min and old_max).
      old_min: The minimum value in the old range.
      old_max: The maximum value in the old range.
      new_min: The minimum value in the new range.
      new_max: The maximum value in the new range.

  Returns:
      The scaled value as an integer within the new range.
  """

  # Check for zero range in the old scale
  if old_max == old_min:
    raise ValueError("Old range cannot be zero")

  # Calculate the scaling factor
  scale_factor = (new_max - new_min) / (old_max - old_min)

  # Scale the value and round to nearest integer
  scaled_val = int(round((val - old_min) * scale_factor) + new_min)

  # Clamp the value to the new range (optional)
  return max(new_min, min(scaled_val, new_max))

# Example usage
old_value = 12  # Value to scale (between 0 and 15)
new_value = scale_value(old_value, 0, 15, 0, 10)
print(new_value)  # Output: 8 (scaled value between 0 and 10)

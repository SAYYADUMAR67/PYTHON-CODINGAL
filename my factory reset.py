def shut_down(s):
  if s.lower() == 'yes':
    return 'Shutting down'
  elif s.lower() == 'no':
    return 'Shutdown aborted'
  else:
    return 'Sorry'
 
 
# Example usage:
print(shut_down('yes'))  # Output: Shutting down
print(shut_down('no'))  # Output: Shutdown aborted
print(shut_down('maybe'))  # Output: Sorry
 
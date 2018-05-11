#
# Soundboard config template
#

# base directory in which all of the sounds reside
sounds_dir: '/etc/soundboard/sounds'

# default volume for sounds to be played at. this helps for "normalization" of various sounds when used in conjunction with
# the volume_boost configuration item. Valid values are 0-100.
default_volume: 25

# if a mapping is not found, this sound file will be played
default_sound: ''

# the volume boost value for the above-configured default sound
# volume boost works by adding the value to the default volume level. However, the max volume is 100, so the resulting
# boosted value will be capped at 100 (i.e. - default: 50 + boost: 75 will still result in 100)
default_sound_volume_boost: 0

# Mapping of keys to sound files. All files are relative to the above-configured sounds_dir.
# Each sound can have a configured volume boost value. See above for volume boost formula
# Key numbers below are based on the midiplus AKM320, available on Amazon
sound_mappings:
  '53': 
    file: ''
    volume_boost: 0
  '54':
    file: ''
  '55':
    file: ''
  '56':
    file: ''
  '57': 
    file: ''
  '58': 
    file: ''
  '59': 
    file: ''
  '60': 
    file: ''
  '61': 
    file: ''
  '62': 
    file: ''
  '63': 
    file: ''
  '64': 
    file: ''
  '65': 
    file: ''
  '66': 
    file: ''
  '67': 
    file: ''
  '68': 
    file: ''
  '69': 
    file: ''
  '70': 
    file: ''
  '71': 
    file: ''
  '72': 
    file: ''
  '73': 
    file: ''
  '74': 
    file: ''
  '75': 
    file: ''
  '76': 
    file: ''
  '77': 
    file: ''
  '78': 
    file: ''
  '79': 
    file: ''
  '80': 
    file: ''
  '81': 
    file: ''
  '82': 
    file: ''
  '83': 
    file: ''
  '84': 
    file: ''

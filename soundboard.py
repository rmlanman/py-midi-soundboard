import os
import yaml
import alsaseq
import pygame

STANDARD_VOLUME = .25

SOUND_KEY_RANGE_MIN = 53
SOUND_KEY_RANGE_MAX = 84

alsaseq.client('Recorder', 1, 0, True)
alsaseq.connectfrom(0, 20, 0)
alsaseq.start()
events = []
pygame.mixer.init()
pygame.mixer.music.set_volume(STANDARD_VOLUME)

config = {}

with open('/etc/soundboard.conf', 'r') as config_file:
    config = yaml.load(config_file)
sound_mappings = config['sound_mappings']

def play_sound(sound, volume):
    path = os.path.join(config['sounds_dir'], sound)
    print "About to play ", path
    print "At volume ", volume
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def is_stop_key(key):
    return STOP_KEY_RANGE_MIN <= key <= STOP_KEY_RANGE_MAX

def is_sound_key(key):
    return SOUND_KEY_RANGE_MIN <= key <= SOUND_KEY_RANGE_MAX

def has_mapping(key):
    return (str(key) in sound_mappings) and ('file' in sound_mappings[str(key)]) and (sound_mappings[str(key)]['file'])

def get_sound(key):
    _sound = config['default_sound']
    if has_mapping(key):
        _sound = sound_mappings[str(key)]['file']

    return _sound

def get_volume(key):
    if not has_mapping(key):
        return STANDARD_VOLUME + (float(config['default_sound_volume_boost'] if 'default_sound_volume_boost' in config else 0) / float(100))
    boost = 0
    if (str(key) in sound_mappings) and ('volume_boost' in sound_mappings[str(key)]) and (sound_mappings[str(key)]['volume_boost']):
        boost = sound_mappings[str(key)]['volume_boost']

    return STANDARD_VOLUME + (float(boost) / float(100))

while 1:
    if alsaseq.inputpending():
        event = alsaseq.input()
        if (event[0] == 13) and (pygame.mixer.music.get_busy()):
            pygame.mixer.music.stop()
            continue
        key = event[7][1]
        if (is_sound_key(key)) and (not pygame.mixer.music.get_busy()):
            sound = get_sound(key)
            volume = get_volume(key)
            play_sound(sound, volume)

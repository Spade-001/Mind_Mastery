import muselsl as muse

muses = muse.list_muses()

muse.stream(muses[0]['address'])


print('Stream has ended')
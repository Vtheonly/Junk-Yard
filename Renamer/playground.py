from rename import list_files_in_directory as ListF
from rename import list_dirs_in_directory as ListD
from rename import rename_folders
from rename import rename_files

directory =r"C:\Users\merse\OneDrive\Documents\Learn\Courses\2 - Engineering\2 - System Design\Systems Design"

# print(ListD(directory))

old = ListF(directory)

print((old))


new  = [
  '1 Introduction.mp4',
 '10 Load Balancers.mp4',
 '11 Hashing.mp4',
 '12 Relational Databases.mp4',
 '13 KeyValue Stores.mp4',
 '14 Replication And Sharding.mp4',
 '15 Leader Election.mp4',
 '16 PeerToPeer Networks.mp4',
 '17 Polling And Streaming.mp4',
 '18 Configuration.mp4',
 '19 Rate Limiting.mp4',
 '2 What Are Design Fundamentals.mp4',
 '20 Logging And Monitoring.mp4',
 '3 ClientвServer Model.mp4',
 '4 Network Protocols.mp4',
 '5 Storage.mp4',
 '6 Latency And Throughput.mp4',
 '7 Availability.mp4',
 '8 Caching.mp4',
 '9 Proxies.mp4'
 ]


# rename_folders(old,new)
rename_files(old,new)


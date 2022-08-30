'''
August 20 for getting the RMSD scores of all mutations
Runtime is around 6 minutes for 109 files against original GFP

Intruction:
1. Downlaod PyMol
2. Check the path, change it to your own path
3. In PyMol: File > RunScript > select this file
'''
from pymol import cmd, stored
import pandas as pd
import os

'''
file paths
'''
# # file path for novel GFPs
# file_path2 = 'C:/Users/annat/OneDrive - University of Toronto/USRP Summer/GitHub/Pardee-Lab-computation-project-pipeline/novel_GFP11_Sequences/'
# file_path = "C:/Users/annat\OneDrive - University of Toronto/USRP Summer/GitHub/Pardee-Lab-computation-project-pipeline/multimer_results/"
# full_gfp = file_path + 'full_GFP.pdb'
#
# # files
# file_names = []
# for file in os.listdir(file_path2):
#     if file.endswith(".pdb"):
#         file_names.append(file_path2 + str(file))
#         # print(os.path.join("/content", file))
# print(file_names)
#
# cmd.load(full_gfp)
#
# all_files = file_names
# for file_n in file_names:
#   all_files.append(file_n)
#   cmd.load(file_n)
#
# # all_files = []
# # for i in range(1,110):
# #   file_name = file_path + f'high_brightness{i}.pdb'
# #   all_files.append(file_name)
# #   cmd.load(file_name)

'''
Function developed by 
http://pldserver1.biochem.queensu.ca/~rlc/work/pymol/align_all.py
'''
def align_all(target=None,mobile_selection='name ca',target_selection='name ca',cutoff=2, cycles=5,cgo_object=0,method='align'):
  cutoff = int(cutoff)
  cycles = int(cycles)
  cgo_object = int(cgo_object)

  object_list = cmd.get_names()
  print('object list =', object_list)
  object_list.remove(target)

  df_rmsd = pd.DataFrame({'File':[],
        'RMSD':[],
        'Number_of_atoms':[]
       })


  rmsd = {}
  rmsd_list = []
  for i in range(len(object_list)):
    if cgo_object:
      objectname = 'align_%s_on_%s' % (object_list[i],target)
      if method == 'align':
        rms = cmd.align('%s & %s'%(object_list[i],mobile_selection),'%s & %s'%(target,target_selection),cutoff=cutoff,cycles=cycles,object=objectname)
      elif method == 'super':
        rms = cmd.super('%s & %s'%(object_list[i],mobile_selection),'%s & %s'%(target,target_selection),cutoff=cutoff,cycles=cycles,object=objectname)
      elif method == 'cealign':
        rmsdict = cmd.cealign('%s & %s' % (target,target_selection),'%s & %s' % (object_list[i],mobile_selection))
        rms = [rmsdict['RMSD'],rmsdict['alignment_length'],1,0,0]
      else:
        print("only 'align', 'super' and 'cealign' are accepted as methods")
        sys.exit(-1)
    else:
      if method == 'align':
        rms = cmd.align('%s & %s'%(object_list[i],mobile_selection),'%s & %s'%(target,target_selection),cutoff=cutoff,cycles=cycles)
      elif method == 'super':
        rms = cmd.super('%s & %s'%(object_list[i],mobile_selection),'%s & %s'%(target,target_selection),cutoff=cutoff,cycles=cycles)
      elif method == 'cealign':
        rmsdict = cmd.cealign('%s & %s' % (target,target_selection),'%s & %s' % (object_list[i],mobile_selection))
        rms = [rmsdict['RMSD'],rmsdict['alignment_length'],1,0,0]
      else:
        print("only 'align', 'super' and 'cealign' are accepted as methods")
        sys.exit(-1)

    rmsd[object_list[i]] = (rms[0],rms[1])
    rmsd_list.append((object_list[i],rms[0],rms[1]))

# sort RMSD_LIST
  rmsd_list.sort(key=lambda x: x[1])
# loop over dictionary and print out matrix of final rms values
  print("Aligning against:",target)
  for object_name in object_list:
    print("%s: %6.3f using %d atoms" % (object_name,rmsd[object_name][0],rmsd[object_name][1]))
    df_rmsd.loc[len(df_rmsd.index)] = [object_name, rmsd[object_name][0],rmsd[object_name][1]]
  print("\nSorted from best match to worst:")
  for r in rmsd_list:
    print("%s: %6.3f using %d atoms" % r)
  df_rmsd.to_csv('align_all.csv')

cmd.extend('align_all',align_all)

align_all('full_GFP')

# f=open('file1.txt','w+')
# f.write('this is 1st file')
# f.close()
# f=open('file2.txt','w+')
# f.write('this is 2nd file')
# f.close()

# import zipfile
# comp_file= zipfile.ZipFile('comp_file.zip','w')
# comp_file.write('file1.txt',compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write('file2.txt',compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()

# unzip= zipfile.ZipFile('comp_file.zip','r')
# unzip.extractall('extractedfile')

import shutil
# folderzip='C:\\Users\\hp\\Documents\\GitHub\\PythonsFiles\\extractedfile'
# outputfilename='outputfolder'
# shutil.make_archive(outputfilename,'zip',folderzip)
shutil.unpack_archive('outputfolder.zip','finalunzipfolder','zip')

import subprocess


subprocess.run('git init')
subprocess.run('git add .')
subprocess.run('git commit -m "init python project"')
subprocess.run('git remote add origin git@github.com:lin-zone/test_travis.git')
subprocess.run('git push -u origin master')

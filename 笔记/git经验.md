https://www.runoob.com/git/git-workflow.html

常用的场景：
1 把远程的项目放在本地
git clone -b <branch_name> <url>
之前需要让编辑器和远程仓库建立连接(https 或 ssh)
https://zhuanlan.zhihu.com/p/656757962

2 本地修改后提交到暂存区
git add

3 提交
git commit
<!-- 前面是在本地操作 -->
4 远程库操作
git push/pull/fetch
git pull=git fetch+git merge

push之前要先pull, 把冲突解决在本地，不要直接覆盖
查看差异
git diff

查看哪些文件被修改
git status 

查看提交历史
git log

4 回退 到之前某一次提交后的状态
git reset soft/hard xxx
https://www.cnblogs.com/miracle-luna/p/13823175.html

5 分支相关
https://www.runoob.com/git/git-branch.html
将其他分支合并到当前分支：
git merge <branchname>
需要解决冲突

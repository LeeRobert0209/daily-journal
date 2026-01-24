import os
import datetime

# 1. 自动获取当前年份，避免明年还要手动改代码
current_year = datetime.date.today().year

# 2. 优化输入提示
input_date = input(f"请输入日期 (格式 MM-DD，如 01-24，直接回车代表今天): ").strip()

if not input_date:
    target_date = datetime.date.today().strftime("%Y-%m-%d")
else:
    # 如果你输入的是 1-24，它会自动变成 2026-1-24
    target_date = f"{current_year}-{input_date}"

commit_msg = f"Doc:更新了{target_date}的五件事"

print(f"--- 🚀 准备上传: {commit_msg} ---")

# 3. 使用更稳健的命令执行方式
os.system("git add .")
# 这里的引号处理是为了防止 Commit 信息中有空格导致报错
exit_code = os.system(f'git commit -m "{commit_msg}"')

if exit_code == 0:
    os.system("git push")
    print(f"\n✅ 任务完成！{target_date} 的记录已同步至 GitHub。")
else:
    print("\n❌ 提交失败：可能是没有检测到文件变更。")
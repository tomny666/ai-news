import yaml

with open('.github/workflows/update-news.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

print('YAML 语法: 有效')
print('工作流名称:', data.get('name'))

triggers = data.get('on', {})
schedule = triggers.get('schedule', [])
if schedule:
    print('定时调度 cron:', schedule[0].get('cron'))

jobs = data.get('jobs', {})
print('Jobs:', list(jobs.keys()))

for name, job in jobs.items():
    steps = job.get('steps', [])
    print(f'\nJob: {name}')
    print(f'  运行环境: {job.get("runs-on")}')
    print(f'  步骤数: {len(steps)}')
    if job.get('needs'):
        print(f'  依赖: {job.get("needs")}')
    for s in steps:
        step_name = s.get('name', '')
        uses = s.get('uses', '')
        run_cmd = s.get('run', '')[:50].replace('\n', ' ')
        detail = uses if uses else run_cmd
        print(f'  - {step_name}: {detail}')

perms = data.get('permissions', {})
print('\nPermissions:', list(perms.keys()) if isinstance(perms, dict) else perms)

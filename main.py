from indeed import get_jobs_data as get_indeed_jobs
from sof import get_jobs_data as get_sof_jobs

indeed_jobs_data = get_indeed_jobs()
sof_jobs_data = get_sof_jobs()
jobs = indeed_jobs_data + sof_jobs_data

print(sof_jobs_data)

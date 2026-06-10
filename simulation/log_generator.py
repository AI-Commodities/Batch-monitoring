#!/usr/bin/env python3
import os
import time
import random
from datetime import datetime

class LogGenerator:
    def __init__(self, log_dir="Sample_logs/"):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        
    def generate_openlink_log(self, status=None):
        if status is None:
            status = random.choice(['SUCCESS', 'FAILED', 'RUNNING'])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        job_names = ['COMMODITY_PRICE', 'OIL_FUTURES', 'GAS_SPOT', 'GOLD_FIXING']
        job_name = random.choice(job_names)
        
        log_content = "[OPENLINK Batch Monitor]\n"
        log_content += f"Timestamp: {timestamp}\n"
        log_content += f"Job Name: {job_name}\n"
        log_content += f"Status: {status}\n"
        log_content += f"Duration: {random.randint(10, 300)} seconds\n"
        log_content += f"Records Processed: {random.randint(100, 10000)}\n"
        log_content += "Details:\n"
        log_content += f"- Started at: {timestamp}\n"
        log_content += "- Connection: OPENLINK_PROD\n"
        log_content += "- Environment: DEV\n"
        
        if status == 'SUCCESS':
            log_content += "SUCCESS: Batch completed successfully\n"
        elif status == 'FAILED':
            log_content += f"ERROR: Failed at {random.randint(1, 100)} percent - Connection timeout\n"
        else:
            log_content += "RUNNING: Batch is currently processing\n"
        
        filename = f"openlink_{job_name}_{timestamp[:10]}.log"
        filepath = os.path.join(self.log_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(log_content)
        
        return filepath, status
    
    def generate_autosys_log(self, status=None):
        if status is None:
            status = random.choice(['SUCCESS', 'FAILURE', 'RUNNING'])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        job_names = ['DAILY_ETL', 'DATA_LOAD', 'REPORT_GEN', 'BACKUP_JOB']
        job_name = random.choice(job_names)
        
        log_content = "# Autosys Job Report\n\n"
        log_content += "## Job Information\n"
        log_content += f"- Job Name: {job_name}\n"
        log_content += f"- Start Time: {timestamp}\n"
        log_content += f"- Status: {status}\n"
        log_content += f"- Exit Code: {0 if status == 'SUCCESS' else random.randint(1, 255)}\n\n"
        log_content += "## Execution Details\n"
        log_content += f"- Machine: autosys-server-{random.randint(1, 5)}\n"
        log_content += "- User: batch_user\n"
        log_content += f"- Command: /opt/scripts/{job_name.lower()}.sh\n\n"
        log_content += "## Log Output\n"
        log_content += f"Processing started at {timestamp}\n"
        log_content += f"Loaded {random.randint(1000, 50000)} records\n"
        
        if status == 'SUCCESS':
            log_content += "Processing completed successfully\n"
        elif status == 'FAILURE':
            log_content += f"ERROR: Failed to process - Exit code {random.randint(1, 255)}\n"
        else:
            log_content += "Job is still running\n"
        
        filename = f"autosys_{job_name}_{timestamp[:10]}.md"
        filepath = os.path.join(self.log_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(log_content)
        
        return filepath, status
    
    def generate_feedtool_log(self, status=None):
        if status is None:
            status = random.choice(['COMPLETED', 'ERROR', 'IN_PROGRESS'])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        feeds = ['Market_Data', 'Reference_Data', 'Price_Feed', 'News_Feed']
        feed_name = random.choice(feeds)
        
        log_content = "[FeedConfigTool] - Feed Processing Log\n"
        log_content += "=========================================\n"
        log_content += f"Feed Name: {feed_name}\n"
        log_content += f"Start Time: {timestamp}\n"
        log_content += f"Status: {status}\n"
        log_content += f"Configuration: config/feeds/{feed_name.lower()}.xml\n\n"
        log_content += "Processing Steps:\n"
        
        if status != 'ERROR':
            log_content += "1. Validating feed configuration... SUCCESS\n"
            log_content += "2. Connecting to data source... SUCCESS\n"
        else:
            log_content += "1. Validating feed configuration... FAILED\n"
        
        if status == 'COMPLETED':
            log_content += "3. Fetching data... SUCCESS\n"
            log_content += "4. Transforming data... SUCCESS\n"
            log_content += "5. Loading to target... SUCCESS\n\n"
            log_content += f"SUCCESS: Feed processing completed: {random.randint(100, 10000)} records loaded\n"
        elif status == 'ERROR':
            log_content += f"ERROR: Feed validation failed - Invalid schema at line {random.randint(1, 100)}\n"
        else:
            log_content += "3. Fetching data... IN_PROGRESS\n"
            log_content += f"IN_PROGRESS: Processing {random.randint(20, 80)} percent complete\n"
        
        filename = f"feedtool_{feed_name.lower()}_{timestamp[:10]}.md"
        filepath = os.path.join(self.log_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(log_content)
        
        return filepath, status
    
    def generate_all_logs(self, count=5):
        print(f"Generating {count} logs of each type...")
        
        results = {'openlink': [], 'autosys': [], 'feedtool': []}
        
        for i in range(count):
            status = random.choice(['SUCCESS', 'FAILED', 'RUNNING'])
            filepath, status_result = self.generate_openlink_log(status)
            results['openlink'].append({'file': filepath, 'status': status_result})
            
            status = random.choice(['SUCCESS', 'FAILURE', 'RUNNING'])
            filepath, status_result = self.generate_autosys_log(status)
            results['autosys'].append({'file': filepath, 'status': status_result})
            
            status = random.choice(['COMPLETED', 'ERROR', 'IN_PROGRESS'])
            filepath, status_result = self.generate_feedtool_log(status)
            results['feedtool'].append({'file': filepath, 'status': status_result})
            
            time.sleep(1)
        
        return results
    
    def generate_failed_logs(self, count=3):
        print(f"Generating {count} failed logs...")
        for i in range(count):
            self.generate_openlink_log('FAILED')
            self.generate_autosys_log('FAILURE')
            self.generate_feedtool_log('ERROR')
            time.sleep(1)
    
    def generate_success_logs(self, count=3):
        print(f"Generating {count} success logs...")
        for i in range(count):
            self.generate_openlink_log('SUCCESS')
            self.generate_autosys_log('SUCCESS')
            self.generate_feedtool_log('COMPLETED')
            time.sleep(1)
    
    def clear_logs(self):
        for file in os.listdir(self.log_dir):
            filepath = os.path.join(self.log_dir, file)
            if os.path.isfile(filepath):
                os.remove(filepath)
        print(f"Cleared all logs from {self.log_dir}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', choices=['generate', 'failed', 'success', 'clear'], default='generate')
    parser.add_argument('--count', type=int, default=5)
    
    args = parser.parse_args()
    generator = LogGenerator()
    
    if args.action == 'generate':
        print("Generating random logs...")
        results = generator.generate_all_logs(args.count)
        print(f"\nSummary: Generated {len(results['openlink'])} OPENLINK, {len(results['autosys'])} Autosys, {len(results['feedtool'])} FeedTool logs")
    
    elif args.action == 'failed':
        generator.generate_failed_logs(args.count)
        print(f"Generated {args.count} failed logs")
    
    elif args.action == 'success':
        generator.generate_success_logs(args.count)
        print(f"Generated {args.count} success logs")
    
    elif args.action == 'clear':
        generator.clear_logs()
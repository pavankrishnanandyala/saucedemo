import os
from datetime import datetime
import getpass
import platform
import sys


class HTMLReportGenerator:
    def __init__(self):
        self.report_dir = "Reports"
        self.timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        self.user = getpass.getuser()

        # Create Reports directory if it doesn't exist
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

    def generate_html_report(self, test_results):
        """Generate HTML report with current date, time and user information."""

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Automation Report - {self.timestamp}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    background-color: #f5f5f5;
                }}
                .header {{
                    background-color: #2c3e50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                    border-radius: 5px;
                    margin-bottom: 20px;
                }}
                .info-section {{
                    background-color: white;
                    padding: 20px;
                    border-radius: 5px;
                    margin-bottom: 20px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .results-table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                    background-color: white;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .results-table th, .results-table td {{
                    padding: 12px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }}
                .results-table th {{
                    background-color: #34495e;
                    color: white;
                }}
                .passed {{ color: #27ae60; }}
                .failed {{ color: #c0392b; }}
                .skipped {{ color: #f39c12; }}
                .summary-box {{
                    background-color: white;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 10px 0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Test Automation Report</h1>
            </div>

            <div class="info-section">
                <h2>Execution Information</h2>
                <p><strong>Date and Time (UTC):</strong> {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p><strong>User:</strong> {self.user}</p>
                <p><strong>Python Version:</strong> {platform.python_version()}</p>
                <p><strong>Platform:</strong> {platform.platform()}</p>
            </div>

            <div class="info-section">
                <h2>Test Summary</h2>
                <div class="summary-box">
                    <p><strong>Total Tests:</strong> {test_results['total']}</p>
                    <p><strong>Passed:</strong> <span class="passed">{test_results['passed']}</span></p>
                    <p><strong>Failed:</strong> <span class="failed">{test_results['failed']}</span></p>
                    <p><strong>Skipped:</strong> <span class="skipped">{test_results['skipped']}</span></p>
                    <p><strong>Pass Rate:</strong> {test_results['pass_rate']:.2f}%</p>
                </div>
            </div>

            <div class="info-section">
                <h2>Test Details</h2>
                <table class="results-table">
                    <tr>
                        <th>Test Case</th>
                        <th>Status</th>
                        <th>Duration (s)</th>
                        <th>Error Message</th>
                    </tr>
                    {self._generate_test_rows(test_results['details'])}
                </table>
            </div>
        </body>
        </html>
        """

        # Write the HTML report
        report_path = os.path.join(self.report_dir, f"test_report_{self.timestamp}.html")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        return report_path

    def _generate_test_rows(self, test_details):
        """Generate HTML table rows for test details."""
        rows = ""
        for test in test_details:
            status_class = test['status'].lower()
            rows += f"""
                <tr>
                    <td>{test['name']}</td>
                    <td class="{status_class}">{test['status']}</td>
                    <td>{test['duration']:.2f}</td>
                    <td>{test.get('error', '-')}</td>
                </tr>
            """
        return rows
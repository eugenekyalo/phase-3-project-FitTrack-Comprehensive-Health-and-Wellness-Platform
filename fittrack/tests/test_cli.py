import subprocess
import unittest

class TestFitTrackCLI(unittest.TestCase):

    def run_cli_command(self, *args):
        result = subprocess.run(['python3', 'fittrack/cli.py'] + list(args), capture_output=True, text=True)
        print(result.stdout)  # Print standard output for debugging
        print(result.stderr)  # Print standard error for debugging
        return result

    def test_set_goal_command(self):
        result = self.run_cli_command('set-goal', '--user_id', '1', '--goal_type', 'weight_loss', '--target_value', '10.0', '--current_value', '5.0')
        self.assertEqual(result.returncode, 0)

    def test_track_command(self):
        result = self.run_cli_command('track', '--user_id', '1', '--weight', '70', '--height', '175')
        self.assertEqual(result.returncode, 0)

    def test_view_journal_command(self):
        result = self.run_cli_command('view-journal')
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()

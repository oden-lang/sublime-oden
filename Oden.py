import sublime_plugin
import subprocess

class RunOdenCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    try:
      result = subprocess.check_output(["oden", "run", "-M", self.view.file_name()], 
                                       stderr=subprocess.STDOUT,
                                       universal_newlines=True)
      self.show_output(result, edit)
    except subprocess.CalledProcessError as e:
      self.show_output(e.output, edit)

  def show_output(self, text, edit):
    v = self.view.window().create_output_panel("Oden Output")
    v.insert(edit, v.size(), text)
    v.show(v.size())
    self.view.window().run_command("show_panel", {"panel": "output.Oden Output"})

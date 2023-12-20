import System.Drawing
import System.Windows.Forms
import Math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(115, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(359, 264)
		self._listBox1.TabIndex = 1
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(100, 40, 120)
		self.ClientSize = System.Drawing.Size(732, 298)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "p122h"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range (1,21):
			num ** num
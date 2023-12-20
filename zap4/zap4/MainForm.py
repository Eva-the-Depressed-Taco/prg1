import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Plum
		self._button1.Location = System.Drawing.Point(47, 24)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 20)
		self._button1.TabIndex = 0
		self._button1.Text = "killwats used"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Pink
		self._label1.Location = System.Drawing.Point(187, 73)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Pink
		self._label2.Location = System.Drawing.Point(187, 185)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Pink
		self._label3.Location = System.Drawing.Point(187, 143)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 3
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Pink
		self._label4.Location = System.Drawing.Point(187, 106)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 4
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Pink
		self._label5.Location = System.Drawing.Point(187, 221)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 5
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Pink
		self._textBox1.Location = System.Drawing.Point(187, 24)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Plum
		self._label6.Location = System.Drawing.Point(47, 221)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 11
		self._label6.Text = "late fee"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Plum
		self._label7.Location = System.Drawing.Point(47, 185)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 10
		self._label7.Text = "total"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Plum
		self._label8.Location = System.Drawing.Point(47, 143)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 9
		self._label8.Text = "city tax"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Plum
		self._label9.Location = System.Drawing.Point(47, 106)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 8
		self._label9.Text = "surcharge"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Plum
		self._label10.Location = System.Drawing.Point(47, 73)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 7
		self._label10.Text = "cost"
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkMagenta
		self.ClientSize = System.Drawing.Size(390, 326)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "zap4"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		zaps = int(self._textBox1.Text)
		bill = zaps * 0.0475
		cityt = bill * 0.03
		scharge = bill * 0.10
		total = bill + cityt + scharge
		latef = total *1.04
		self._label1.Text = str(round(bill,2))
		self._label4.Text = str(round(scharge,2))
		self._label3.Text = str(round(cityt,2))
		self._label2.Text = str(round(total,2))
		self._label5.Text = str(round(latef,2))
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.num1 = 0
		self.num3 = 0
		self.num2 = 0
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._pictureBox3 = System.Windows.Forms.PictureBox()
		self._progressBar1 = System.Windows.Forms.ProgressBar()
		self._pictureBox4 = System.Windows.Forms.PictureBox()
		self._pictureBox5 = System.Windows.Forms.PictureBox()
		self._pictureBox6 = System.Windows.Forms.PictureBox()
		self._pictureBox7 = System.Windows.Forms.PictureBox()
		self._pictureBox8 = System.Windows.Forms.PictureBox()
		self._pictureBox9 = System.Windows.Forms.PictureBox()
		self._pictureBox10 = System.Windows.Forms.PictureBox()
		self._pictureBox11 = System.Windows.Forms.PictureBox()
		self._timer1 = System.Windows.Forms.Timer(self._components)
		self._pictureBox1.BeginInit()
		self._pictureBox2.BeginInit()
		self._pictureBox3.BeginInit()
		self._pictureBox4.BeginInit()
		self._pictureBox5.BeginInit()
		self._pictureBox6.BeginInit()
		self._pictureBox7.BeginInit()
		self._pictureBox8.BeginInit()
		self._pictureBox9.BeginInit()
		self._pictureBox10.BeginInit()
		self._pictureBox11.BeginInit()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(437, 23)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(131, 145)
		self._button1.TabIndex = 0
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(437, 193)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "pickpocket"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(518, 193)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "bet"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(607, 233)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "100"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(531, 233)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(70, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "cash"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(624, 195)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		# 
		# pictureBox1
		# 
		self._pictureBox1.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox1.Location = System.Drawing.Point(12, 23)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(123, 145)
		self._pictureBox1.TabIndex = 6
		self._pictureBox1.TabStop = False
		# 
		# pictureBox2
		# 
		self._pictureBox2.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox2.Location = System.Drawing.Point(291, 23)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(123, 145)
		self._pictureBox2.TabIndex = 7
		self._pictureBox2.TabStop = False
		# 
		# pictureBox3
		# 
		self._pictureBox3.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox3.Location = System.Drawing.Point(151, 23)
		self._pictureBox3.Name = "pictureBox3"
		self._pictureBox3.Size = System.Drawing.Size(123, 145)
		self._pictureBox3.TabIndex = 8
		self._pictureBox3.TabStop = False
		# 
		# progressBar1
		# 
		self._progressBar1.Location = System.Drawing.Point(531, 267)
		self._progressBar1.Maximum = 15000
		self._progressBar1.Name = "progressBar1"
		self._progressBar1.Size = System.Drawing.Size(100, 23)
		self._progressBar1.TabIndex = 9
		self._progressBar1.Click += self.ProgressBar1Click
		# 
		# pictureBox4
		# 
		self._pictureBox4.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox4.Location = System.Drawing.Point(12, 174)
		self._pictureBox4.Name = "pictureBox4"
		self._pictureBox4.Size = System.Drawing.Size(402, 145)
		self._pictureBox4.TabIndex = 10
		self._pictureBox4.TabStop = False
		# 
		# pictureBox5
		# 
		self._pictureBox5.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox5.Location = System.Drawing.Point(257, 181)
		self._pictureBox5.Name = "pictureBox5"
		self._pictureBox5.Size = System.Drawing.Size(32, 34)
		self._pictureBox5.TabIndex = 11
		self._pictureBox5.TabStop = False
		# 
		# pictureBox6
		# 
		self._pictureBox6.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox6.Location = System.Drawing.Point(219, 181)
		self._pictureBox6.Name = "pictureBox6"
		self._pictureBox6.Size = System.Drawing.Size(32, 34)
		self._pictureBox6.TabIndex = 12
		self._pictureBox6.TabStop = False
		# 
		# pictureBox7
		# 
		self._pictureBox7.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox7.Location = System.Drawing.Point(181, 181)
		self._pictureBox7.Name = "pictureBox7"
		self._pictureBox7.Size = System.Drawing.Size(32, 34)
		self._pictureBox7.TabIndex = 13
		self._pictureBox7.TabStop = False
		self._pictureBox7.Click += self.PictureBox7Click
		# 
		# pictureBox8
		# 
		self._pictureBox8.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox8.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox8.Location = System.Drawing.Point(143, 182)
		self._pictureBox8.Name = "pictureBox8"
		self._pictureBox8.Size = System.Drawing.Size(32, 34)
		self._pictureBox8.TabIndex = 14
		self._pictureBox8.TabStop = False
		# 
		# pictureBox9
		# 
		self._pictureBox9.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox9.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox9.Location = System.Drawing.Point(105, 182)
		self._pictureBox9.Name = "pictureBox9"
		self._pictureBox9.Size = System.Drawing.Size(32, 34)
		self._pictureBox9.TabIndex = 15
		self._pictureBox9.TabStop = False
		# 
		# pictureBox10
		# 
		self._pictureBox10.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox10.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox10.Location = System.Drawing.Point(67, 181)
		self._pictureBox10.Name = "pictureBox10"
		self._pictureBox10.Size = System.Drawing.Size(32, 34)
		self._pictureBox10.TabIndex = 16
		self._pictureBox10.TabStop = False
		# 
		# pictureBox11
		# 
		self._pictureBox11.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._pictureBox11.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox11.Location = System.Drawing.Point(35, 181)
		self._pictureBox11.Name = "pictureBox11"
		self._pictureBox11.Size = System.Drawing.Size(26, 34)
		self._pictureBox11.TabIndex = 17
		self._pictureBox11.TabStop = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(741, 313)
		self.Controls.Add(self._pictureBox11)
		self.Controls.Add(self._pictureBox10)
		self.Controls.Add(self._pictureBox9)
		self.Controls.Add(self._pictureBox8)
		self.Controls.Add(self._pictureBox7)
		self.Controls.Add(self._pictureBox6)
		self.Controls.Add(self._pictureBox5)
		self.Controls.Add(self._pictureBox4)
		self.Controls.Add(self._progressBar1)
		self.Controls.Add(self._pictureBox3)
		self.Controls.Add(self._pictureBox2)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "slot1"
		self.Load += self.MainFormLoad
		self._pictureBox1.EndInit()
		self._pictureBox2.EndInit()
		self._pictureBox3.EndInit()
		self._pictureBox4.EndInit()
		self._pictureBox5.EndInit()
		self._pictureBox6.EndInit()
		self._pictureBox7.EndInit()
		self._pictureBox8.EndInit()
		self._pictureBox9.EndInit()
		self._pictureBox10.EndInit()
		self._pictureBox11.EndInit()
		self.ResumeLayout(False)
		self.PerformLayout()


	def ProgressBar1Click(self, sender, e):
		pass

	def PictureBox7Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		rnd = System.Random()
		money = rnd.Next(1, 51)
		if money is > 25:
			MessageBox.Show("you failed to steal money")
		if money is > 49:
			MessageBox.Show("you where caught stealing and where punched in the face mutiple times")
		else:
			cmoney = float(self._label2.Text)
			self._label2.Text = str(round(cmoney + money, 2))
			

	def Button1Click(self, sender, e):
		im1 = self.pictureBox5.BackroundImage
		im2 = self.pictureBox6.BackroundImage
		im3 = self.pictureBox7.BackroundImage
		im4 = self.pictureBox8.BackroundImage
		im5 = self.pictureBox9.BackroundImage
		levOff = self.pictureBox10.BackroundImage
		levOn = self.pictureBox11.BackroundImage
		num1 = 0
		num2 = 0
		num2 = 0
		
		if self._textBox1.Text = "":
			MessageBox.Show(Enter bet first)
			
		money = float(self._label2.Text)
		bet = float(self._textBox1.Text)
		money2 = money - bet
		if money == 0:
			Messagebox.Show("you have no money)
			elif bet < 1:
				MessageBox.Show("enter atleast 1 dollar)
			elif bet < 
		
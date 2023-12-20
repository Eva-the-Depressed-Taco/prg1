require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.MediumOrchid
		@button1.Location = System::Drawing::Point.new(138, 66)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 0
		@button1.Text = "show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.MediumPurple
		@button2.Location = System::Drawing::Point.new(138, 96)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 1
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.MediumPurple
		@label1.Location = System::Drawing::Point.new(252, 66)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 305)
		@label1.TabIndex = 2
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.DeepPink
		self.ClientSize = System::Drawing::Size.new(967, 453)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "phonenumbersthisoneforrealsies"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "608 354 6783 \n 679 357 3617 \n 579 448 4738 \n 608 555 9373 \n 677 567 3777"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end

	def MainFormLoad(sender, e)
		
	end

	def Label1Click(sender, e)
		
	end
end


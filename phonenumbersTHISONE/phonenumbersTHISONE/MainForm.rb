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
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.DeepSkyBlue
		@button1.Location = System::Drawing::Point.new(143, 196)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 0
		@button1.Text = "show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.DeepSkyBlue
		@button2.Location = System::Drawing::Point.new(143, 138)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 1
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.DeepSkyBlue
		@button3.Location = System::Drawing::Point.new(250, 61)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(441, 323)
		@button3.TabIndex = 2
		@button3.Text = "button3"
		@button3.UseVisualStyleBackColor = false
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.DeepPink
		self.ClientSize = System::Drawing::Size.new(981, 466)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "phonenumbersTHISONE"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
	end

	def MainFormLoad(sender, e)
		
	end

	def Button2Click(sender, e)
		
	end

	def Button1Click(sender, e)
		@label1.Text = " 508 888 7633 \n 768 689 6788 \n 684 858 6392 \n 986 888 9231 \n 449 4578 4829 \n 472 5891 3221
	end
end


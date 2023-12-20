require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.SlateBlue
		@label1.ForeColor = System::Drawing::Color.HotPink
		@label1.Location = System::Drawing::Point.new(69, 48)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(376, 114)
		@label1.TabIndex = 0
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Thistle
		@button1.Location = System::Drawing::Point.new(58, 206)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 1
		@button1.Text = "1 sentace?"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Thistle
		@button2.Cursor = System::Windows::Forms::Cursors.AppStarting
		@button2.Location = System::Drawing::Point.new(174, 205)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 2
		@button2.Text = "no sentace!"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Plum
		self.ClientSize = System::Drawing::Size.new(961, 450)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "ihateaboutme"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = " Im Eva, I make very resposible choicses without execption."
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end


from openai import OpenAI


if __name__ == "__main__":
    # 初始化消息列表
    messages = []
    model_name =['deepseek-reasoner', 'deepseek-chat']
    prompt = ''
    print("********************************************************************************************\n欢迎使用智能助手,基于Deepseek-R1,并支持多轮对话。\n(输入exit退出)\n(输入clear重置)")
    api = input("请输入你的DeepseekAPI:")
    model_num = 999
    # 初始化 OpenAI 客户端
    client = OpenAI(api_key=api, base_url="https://api.deepseek.com")
    while True:
        model_num = int(input("请选择模型: \ndeepseek-reason.............. 0\ndeepseek-chat................ 1\n"))
        if model_num == 0 or model_num == 1:
            break
    while True:
        model_temperature = float(input("请选择功能: \n数学、代码................... 0\n通用对话、翻译................ 1.3\n创意类写作................... 1.5\n"))
        if model_temperature == 0 or model_temperature == 1.3 or model_temperature == 1.5:
            break

    while True:
        count = 0
        # 获取用户输入
        user_input = input("\n\n********************************************************************************************\n请输入你的问题:")
        # 检查用户是否想退出
        if user_input.lower() == "exit":
            print("ByeBye!")
            break
        if user_input.lower() == "clear":
            print("重置对话!")
            messages = []
            continue

        user_input = prompt + user_input
        count += len(user_input)

        # 检查输入是否超过 2000 字
        if count > 5000:
            print("输入超过 5000 字，对话将重新开始。")
            messages = []  # 刷新对话
            count = 0
            continue
        # 添加用户消息到消息列表
        messages.append({"role": "user", "content": user_input})
        try:
            # 调用 API 获取回复
            response = client.chat.completions.create(
                model=model_name[model_num],
                messages=messages,
                temperature= model_temperature
            )
            # 获取回复消息
            assistant_message = response.choices[0].message.to_dict()
            content = response.choices[0].message.content
            if model_num == 0:
                reasoning_content = response.choices[0].message.reasoning_content
                print(f"********************************************************************************************\n思考:\n{reasoning_content}")
            messages.append({"role": "assistant", "content": content})
            print(f"********************************************************************************************\n回答:\n{content}")
            count += len(content)

            # 打印最新一轮的消息
            # print(f"Messages: {messages}")

        except Exception as e:
            print(f"发生错误: {e},\n请检查API是否正确")

def deepseek(input):
    client = OpenAI(api_key="sk-c428611f884e48a08ad2bb1815f0c656", base_url="https://api.deepseek.com")
    # 初始化消息列表
    messages = []
    prompt = ''
    messages.append({"role": "user", "content": prompt + input})
    try:
        # 调用 API 获取回复
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=messages,
            temperature=0.5
        )
        # 获取回复消息
        assistant_message = response.choices[0].message.to_dict()
        content = response.choices[0].message.content
        reasoning_content = response.choices[0].message.reasoning_content
        print(f"思考中:{reasoning_content}")
        print(f"回答：{content}")
        return content

    except Exception as e:
        print(f"发生错误: {e}")

    return "error!"


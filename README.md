# AsiaCell Payment Gateway for Odoo

### Overview
This module integrates the **AsiaCell Payment Gateway** with **Odoo**, allowing you to process payments easily using AsiaCell's "Abayilham" service. This payment gateway allows users to pay amounts via their mobile phones using their balance with AsiaCell.

### Features:
- **Mobile Payment Support**: Customers can make payments using their mobile phones via their AsiaCell balance.
- **Easy Customization**: You can easily customize settings like the API key and the gateway URL.
- **Flexible User Experience**: Users can complete payments simply via an easy-to-use payment interface.

### Requirements:
- You need to have **Odoo** installed.
- You need to have your **API key** from AsiaCell.
- You must have an **AsiaCell account** to obtain your API key.

### Installation:
1. **Add the module file to the `addons` folder in Odoo.**
2. Restart the Odoo server.
3. Go to the **Apps** menu and search for **AsiaCell Payment Gateway**.
4. Install the module.

### Usage:
- After installation, you can configure the gateway by going to **Accounting** > **Payment Settings**.
- There are several configuration options:
  - **API Key**: Enter your API key obtained from AsiaCell.
  - **API URL**: Enter the URL of the API endpoint.

### Configuration:
Once installed, you can customize the settings through the Odoo system settings:
1. **API Key**: Enter the API key provided by AsiaCell.
2. **API URL**: Enter the API URL endpoint to interact with the payment gateway.

### How Payments Work with AsiaCell:
- Once configured, you can start accepting payments via the AsiaCell gateway.
- When a customer selects **Pay with AsiaCell**, they will be directed to an interface where they can input the amount and their mobile phone number.
- Once confirmed, the payment will be processed through the AsiaCell API to verify the transaction.

### Key Files:
1. **`models/payment_gateway.py`**: Contains the logic for integrating the payment gateway.
2. **`views/payment_gateway_views.xml`**: Contains the user interface for configuring the payment gateway.
3. **`controllers/main.py`**: Handles transactions and communicates with the API.
4. **`templates/payment_gateway_templates.xml`**: Contains HTML templates to display the payment form.

### Contribution:
If you wish to contribute to the development of this module or have any suggestions, feel free to open a **pull request** or submit an **issue** via GitHub.

### License:
This project is licensed under the **GPL-2 License**.

---

### Notes:
- If you face any issues while using this module, you can open an **issue** on the GitHub repository and we will assist you in resolving it.




# بوابة الدفع آسيا سيل لأودو

### نظرة عامة
هذه الإضافة تتيح لك دمج بوابة الدفع **آسيا سيل** مع نظام **أودو**، مما يتيح لك معالجة المدفوعات بسهولة باستخدام خدمة "عبّيلهم" من آسيا سيل. تتيح هذه البوابة للمستخدمين دفع المبالغ عبر هواتفهم باستخدام رصيدهم في آسيا سيل.

### المزايا:
- **دعم المدفوعات عبر الهاتف**: يمكن للعملاء دفع المبالغ باستخدام هواتفهم المحمولة عبر رصيدهم في آسيا سيل.
- **تخصيص سهل**: يمكن تخصيص الإعدادات مثل مفتاح الـ API و URL الخاص بالبوابة.
- **تجربة مستخدم مرنة**: يمكن للمستخدمين إتمام الدفع ببساطة باستخدام واجهة دفع سهلة.

### المتطلبات:
- يجب أن يكون لديك نظام **أودو** مثبتاً لديك.
- تحتاج إلى مفتاح الـ API الخاص بك من آسيا سيل.
- يجب أن يكون لديك حساب مع **آسيا سيل** للحصول على مفتاح API الخاص بك.

### التثبيت:
1. **إضافة ملف الـ Module إلى مجلد `addons` في أودو.**
2. قم بإعادة تشغيل خادم أودو.
3. انتقل إلى **التطبيقات** وابحث عن **بوابة الدفع آسيا سيل**.
4. قم بتثبيت الإضافة.

### كيفية الاستخدام:
- بعد تثبيت الإضافة، يمكنك تكوينها عن طريق الذهاب إلى **المالية** > **إعدادات الدفع**.
- هناك عدة خيارات للإعدادات:
  - **مفتاح الـ API**: أدخل مفتاح الـ API الخاص بك من آسيا سيل.
  - **عنوان URL الخاص بـ API**: أدخل عنوان URL للـ API.

### التكوين:
بمجرد التثبيت، يمكنك تخصيص الإعدادات من خلال إعدادات النظام في أودو:
1. **مفتاح الـ API**: أدخل مفتاح الـ API الذي حصلت عليه من آسيا سيل.
2. **عنوان URL للـ API**: أدخل عنوان الـ API الذي ستتواصل معه المدفوعات.

### كيفية الدفع عبر آسيا سيل:
- بعد تكوين البوابة، يمكنك البدء في قبول المدفوعات عبر بوابة آسيا سيل.
- عندما يختار العميل **الدفع باستخدام آسيا سيل**، سيتم توجيههم إلى واجهة حيث يمكنهم إدخال المبلغ ورقم الهاتف المحمول.
- بمجرد التأكيد، سيتم الاتصال بـ API من آسيا سيل للتحقق من المعاملة.

### الملفات الرئيسية:
1. **`models/payment_gateway.py`**: يحتوي على منطق العمل لدمج بوابة الدفع.
2. **`views/payment_gateway_views.xml`**: يحتوي على واجهة المستخدم لإعداد بوابة الدفع.
3. **`controllers/main.py`**: يتعامل مع المعاملات ويدير الاتصال مع API.
4. **`templates/payment_gateway_templates.xml`**: يحتوي على قوالب HTML لعرض نموذج الدفع.

### المساهمة:
إذا كنت ترغب في المساهمة في تطوير هذه الإضافة أو لديك أي اقتراحات، يمكنك فتح **طلب سحب** أو تقديم **مشكلة** عبر GitHub.

### ترخيص:
تم ترخيص هذا المشروع بموجب **ترخيص GPL-2**.

---

### ملاحظات:
- إذا واجهت أي مشاكل أثناء استخدام هذه الإضافة، يمكنك فتح **مشكلة** في مستودع GitHub وسنقوم بمساعدتك في حلها.

from django.core.management.base import BaseCommand
import os
import json

class Command(BaseCommand):
    help = 'Creates translation files for the website'

    def handle(self, *args, **kwargs):
        translations = {
            'fr': {  # French
                'about_us': 'À propos de nous',
                'welcome_message': 'Bienvenue chez InoKit, votre destination privilégiée pour les composants électroniques.',
                'our_mission': 'Notre Mission',
                'mission_statement': 'Fournir des composants électroniques de haute qualité et un service exceptionnel aux amateurs, professionnels et passionnés.',
                'what_we_offer': 'Ce que nous offrons',
                'offer_components': 'Large gamme de composants électroniques',
                'offer_quality': 'Produits de qualité garantie',
                'offer_prices': 'Prix compétitifs',
                'offer_support': 'Support expert',
                'offer_shipping': 'Livraison rapide',
                'contact_us': 'Contactez-nous',
                'address': 'Adresse',
                'phone': 'Téléphone',
                'email': 'Email',
                'business_hours': 'Heures d\'ouverture',
                'weekday_hours': 'Lundi - Vendredi: 9h00 - 18h00',
                'saturday_hours': 'Samedi: 10h00 - 16h00',
                'sunday_hours': 'Dimanche: Fermé',
                'our_products': 'Nos Produits',
                'browse_collection': 'Parcourez notre collection de composants électroniques',
                'price': 'Prix',
                'view_details': 'Voir les détails',
                'add_to_cart': 'Ajouter au panier',
                'no_products': 'Aucun produit disponible pour le moment.',
                'search_placeholder': 'Rechercher des produits...',
                'products': 'Produits',
                'categories': 'Catégories',
                'about': 'À propos',
                'contact': 'Contact',
                'featured_products': 'Produits Vedettes',
                'dev_boards': 'Cartes de développement',
                'dev_boards_desc': 'Arduino, Raspberry Pi, et plus',
                'components': 'Composants électroniques',
                'components_desc': 'Résistances, condensateurs, circuits intégrés',
                'tools': 'Outils et équipements',
                'tools_desc': 'Outils de soudage, multimètres',
                'stock_status': 'État du stock',
                'in_stock': 'En stock',
                'available': 'disponible',
                'out_of_stock': 'Rupture de stock',
                'quantity': 'Quantité',
                'login': 'Connexion',
                'username': 'Nom d\'utilisateur',
                'password': 'Mot de passe',
                'login_error': 'Veuillez entrer un nom d\'utilisateur et un mot de passe corrects. Notez que les deux champs peuvent être sensibles à la casse.',
                'login_button': 'Se connecter',
                'no_account': 'Vous n\'avez pas de compte?',
                'register_now': 'Inscrivez-vous maintenant',
                'our_team': 'Notre Équipe',
                'team_lead': 'Chef d\'équipe',
                'developer': 'Développeur',
                'omar_role': 'Développeur Full Stack & Chef de Projet',
                'omar_desc': 'Dirige le développement d\'InoKit avec une expertise en technologies frontend et backend.',
                'zakaria_role': 'Développeur Backend',
                'zakaria_desc': 'Spécialisé dans le développement backend et la gestion de bases de données.',
                'asia_role': 'Développeuse Frontend',
                'asia_desc': 'Se concentre sur la création d\'interfaces utilisateur belles et réactives.',
            },
            'ar': {  # Arabic
                'about_us': 'معلومات عنا',
                'welcome_message': 'مرحباً بكم في InoKit، وجهتكم المفضلة للمكونات الإلكترونية.',
                'our_mission': 'مهمتنا',
                'mission_statement': 'توفير مكونات إلكترونية عالية الجودة وخدمة استثنائية للهواة والمحترفين.',
                'what_we_offer': 'ما نقدمه',
                'offer_components': 'مجموعة واسعة من المكونات الإلكترونية',
                'offer_quality': 'منتجات مضمونة الجودة',
                'offer_prices': 'أسعار تنافسية',
                'offer_support': 'دعم خبير',
                'offer_shipping': 'شحن سريع',
                'contact_us': 'اتصل بنا',
                'address': 'العنوان',
                'phone': 'الهاتف',
                'email': 'البريد الإلكتروني',
                'business_hours': 'ساعات العمل',
                'weekday_hours': 'الإثنين - الجمعة: 9:00 صباحاً - 6:00 مساءً',
                'saturday_hours': 'السبت: 10:00 صباحاً - 4:00 مساءً',
                'sunday_hours': 'الأحد: مغلق',
                'our_products': 'منتجاتنا',
                'browse_collection': 'تصفح مجموعتنا من المكونات الإلكترونية',
                'price': 'السعر',
                'view_details': 'عرض التفاصيل',
                'add_to_cart': 'أضف إلى السلة',
                'no_products': 'لا توجد منتجات متاحة حالياً.',
                'search_placeholder': 'البحث عن المنتجات...',
                'products': 'المنتجات',
                'categories': 'الفئات',
                'about': 'عن الشركة',
                'contact': 'اتصل بنا',
                'featured_products': 'المنتجات المميزة',
                'dev_boards': 'لوحات التطوير',
                'dev_boards_desc': 'أردوينو، راسبيري باي، والمزيد',
                'components': 'المكونات الإلكترونية',
                'components_desc': 'مقاومات، مكثفات، دوائر متكاملة',
                'tools': 'الأدوات والمعدات',
                'tools_desc': 'أدوات اللحام، أجهزة قياس متعددة',
                'stock_status': 'حالة المخزون',
                'in_stock': 'متوفر',
                'available': 'متاح',
                'out_of_stock': 'نفذ من المخزون',
                'quantity': 'الكمية',
                'login': 'تسجيل الدخول',
                'username': 'اسم المستخدم',
                'password': 'كلمة المرور',
                'login_error': 'الرجاء إدخال اسم المستخدم وكلمة المرور الصحيحين. يرجى ملاحظة أن كلا الحقلين قد يكونان حساسين لحالة الأحرف.',
                'login_button': 'تسجيل الدخول',
                'no_account': 'ليس لديك حساب؟',
                'register_now': 'سجل الآن',
                'our_team': 'فريقنا',
                'team_lead': 'قائد الفريق',
                'developer': 'مطور',
                'omar_role': 'مطور الويب الشامل وقائد المشروع',
                'omar_desc': 'يقود تطوير InoKit مع خبرة في تقنيات الواجهة الأمامية والخلفية.',
                'zakaria_role': 'مطور الخلفية',
                'zakaria_desc': 'متخصص في تطوير الخلفية وإدارة قواعد البيانات.',
                'asia_role': 'مطورة الواجهة الأمامية',
                'asia_desc': 'تركز على إنشاء واجهات مستخدم جميلة وسريعة الاستجابة.',
            },
            'am': {  # Tamazight (Berber)
                'about_us': 'Fell-aɣ',
                'welcome_message': 'Ansuf ɣer InoKit, amḍiq-nwen amezwaru i yiferdisen iliktruniyen.',
                'our_mission': 'Tuɣdaḍt-nneɣ',
                'mission_statement': 'Ad d-nefk iferdisen iliktruniyen n tɣara tafellayt d umeyyez yelhan i yimaziɣen.',
                'what_we_offer': 'Ayen i d-nettakk',
                'offer_components': 'Aṭas n yiferdisen iliktruniyen',
                'offer_quality': 'Ifarisen n tɣara',
                'offer_prices': 'Ssuma yelhan',
                'offer_support': 'Tallelt n yimassanen',
                'offer_shipping': 'Asiweḍ arurad',
                'contact_us': 'Nermes-aɣ-d',
                'address': 'Tansa',
                'phone': 'Tilifun',
                'email': 'Imayl',
                'business_hours': 'Isragen n umahil',
                'weekday_hours': 'Arim - Sem: 9:00 - 18:00',
                'saturday_hours': 'Sed: 10:00 - 16:00',
                'sunday_hours': 'Acer: Imdel',
                'our_products': 'Ifarisen-nneɣ',
                'browse_collection': 'Sken-d tagrumma n yiferdisen iliktruniyen',
                'price': 'Ssuma',
                'view_details': 'Wali ugar',
                'add_to_cart': 'Rnu ɣer tqecwaḍt',
                'no_products': 'Ulac ifarisen akka tura.',
                'search_placeholder': 'Nadi ɣef yifarisen...',
                'products': 'Ifarisen',
                'categories': 'Taggayin',
                'about': 'Fell-aɣ',
                'contact': 'Nermes-aɣ-d',
                'featured_products': 'Ifarisen yettwafren',
                'dev_boards': 'Tifelwiyin n tneflit',
                'dev_boards_desc': 'Arduino, Raspberry Pi, d wiyaḍ',
                'components': 'Iferdisen iliktruniyen',
                'components_desc': 'Timqucac, ikapasiyen, CC',
                'tools': 'Ifecka d wallalen',
                'tools_desc': 'Ifecka n usemlili, multimètres',
                'stock_status': 'Addad n uselɣas',
                'in_stock': 'Yella di uselɣas',
                'available': 'yellan',
                'out_of_stock': 'Ulac-it di uselɣas',
                'quantity': 'Tanecta',
                'login': 'Kcem',
                'username': 'Isem n useqdac',
                'password': 'Awal uffir',
                'login_error': 'Ma ulac aɣilif sekcem isem n useqdac d wawal uffir iṣeḥḥan. Ẓer belli sin n yiḥricen zemren ad ilin d iḥulfan i tira n isekkilen.',
                'login_button': 'Kcem',
                'no_account': 'Ur ɣur-k ara amiḍan?',
                'register_now': 'Jerred tura',
                'our_team': 'Tarbaɛt-nneɣ',
                'team_lead': 'Anemhal n tarbaɛt',
                'developer': 'Aneflay',
                'omar_role': 'Aneflay n Web & Anemhal n usenfar',
                'omar_desc': 'Yettawi asnefli n InoKit s tmusni deg tetiknulujiyin n wudem d deffir.',
                'zakaria_role': 'Aneflay n deffir',
                'zakaria_desc': 'Yettwassen deg usnefli n deffir d usefrek n taffiwin n isefka.',
                'asia_role': 'Taneflayt n wudem',
                'asia_desc': 'Tettarra lwelha i tmerna n wudmawen ifulkiten d yettarra-d s zreb.',
            }
        }

        # Create the translations directory if it doesn't exist
        translations_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'static', 'js', 'translations')
        os.makedirs(translations_dir, exist_ok=True)

        # Write each language file
        for lang_code, translations_dict in translations.items():
            file_path = os.path.join(translations_dir, f'{lang_code}.json')
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(translations_dict, f, ensure_ascii=False, indent=2)
            
            self.stdout.write(self.style.SUCCESS(f'Created translation file for {lang_code}')) 
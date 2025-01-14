import streamlit as st

# Dictionary of 20 digital marketing topics and their descriptions
TOPICS = {
    "1. SEO (Search Engine Optimization)": """
**SEO** stands for Search Engine Optimization. 
It involves optimizing your website and content to rank higher on search engines like Google. 
By using relevant keywords, creating high-quality content, and ensuring a good user experience, 
SEO can increase the visibility of your brand and drive organic traffic.
""",
    "2. SEM (Search Engine Marketing)": """
**SEM** uses paid advertisements that appear on search engine results pages (SERPs). 
Advertisers bid on keywords that users might enter when looking for certain products or services, 
giving the advertiser the opportunity for their ads to appear alongside results for those search queries.
""",
    "3. Social Media Marketing": """
**Social Media Marketing** involves creating and sharing content on social media platforms 
(Facebook, Instagram, Twitter, LinkedIn, etc.) to achieve marketing and branding goals. 
It includes posting text and image updates, videos, and other content that drives audience engagement.
""",
    "4. Content Marketing": """
**Content Marketing** focuses on creating, publishing, and distributing valuable content 
(e.g., blog posts, eBooks, videos, infographics) to attract, engage, and retain a target audience. 
The ultimate goal is to drive profitable customer action.
""",
    "5. Email Marketing": """
**Email Marketing** is the practice of sending targeted messages or newsletters to subscribers 
in order to nurture leads, build relationships, and encourage customer loyalty and repeat business.
""",
    "6. Influencer Marketing": """
**Influencer Marketing** leverages influential people or personalities in a particular niche 
to drive your brand’s message to a larger market. These influencers often have built-in trust 
with their followers, making their endorsements powerful.
""",
    "7. Affiliate Marketing": """
**Affiliate Marketing** is a performance-based marketing model where a business rewards 
affiliates for each visitor or customer brought by the affiliate's own marketing efforts. 
It’s a revenue-sharing model often used in e-commerce.
""",
    "8. Mobile Marketing": """
**Mobile Marketing** focuses on reaching target audiences on their smartphones or tablets 
via mobile apps, mobile-optimized websites, SMS campaigns, or push notifications.
""",
    "9. Display Advertising": """
**Display Advertising** uses visually engaging ads (banners, images, text) 
placed on websites, apps, or social media. The goal is to increase brand awareness 
and drive traffic to your site.
""",
    "10. Marketing Analytics": """
**Marketing Analytics** is the practice of measuring, managing, and analyzing marketing performance 
to maximize effectiveness and optimize return on investment (ROI). 
It enables marketers to be more efficient at their jobs.
""",
    "11. Conversion Rate Optimization (CRO)": """
**Conversion Rate Optimization** focuses on increasing the percentage of website or app visitors 
who take a desired action—such as filling out a form, signing up for a trial, or making a purchase.
""",
    "12. E-commerce Marketing": """
**E-commerce Marketing** involves strategies for driving online sales, 
ranging from optimizing product listings, using paid advertising, 
implementing email and social media campaigns, to ensuring a great user experience.
""",
    "13. Growth Hacking": """
**Growth Hacking** is a process of rapid experimentation across marketing channels 
and product development to identify the most effective ways to grow a business. 
It often involves creative, low-cost strategies.
""",
    "14. Video Marketing": """
**Video Marketing** involves using video content to promote or market a brand, product, or service. 
It can be published on various platforms, including websites, YouTube, and social media.
""",
    "15. Podcast Advertising": """
**Podcast Advertising** leverages the power of audio content. Brands sponsor or run ads during podcasts 
to reach engaged audiences who trust and identify with the podcast hosts.
""",
    "16. Marketing Automation": """
**Marketing Automation** uses software to automate repetitive marketing tasks, 
such as email campaigns, social media posting, and ad management, 
to increase efficiency and personalize the customer experience.
""",
    "17. Web Analytics": """
**Web Analytics** tracks and analyzes website traffic to understand user behavior, 
improve user experience, and optimize digital marketing strategies and ROI.
""",
    "18. Online Reputation Management (ORM)": """
**Online Reputation Management** involves controlling and improving how your brand is perceived online. 
It includes monitoring mentions, managing reviews, and effectively responding to positive or negative feedback.
""",
    "19. Webinars and Online Events": """
**Webinars and Online Events** are live or recorded events conducted online 
to educate, inform, or demonstrate products to an audience, 
often with interactive elements like Q&A sessions.
""",
    "20. Inbound Marketing": """
**Inbound Marketing** focuses on attracting customers by creating valuable content and experiences 
tailored to them. It pulls in potential customers rather than pushing out messages to a broad audience.
"""
}


def show_main_page():
    """Render the main page with 20 topic buttons in three columns."""
    st.title("Digital Marketing Topics")
    st.write("Select a topic to learn more:")

    col1, col2, col3 = st.columns(3)
    topics = list(TOPICS.keys())

    # Distribute buttons in three columns
    for i, topic in enumerate(topics):
        if i % 3 == 0:
            with col1:
                if st.button(topic, key=f"btn_{topic}"):
                    st.session_state.page = topic
        elif i % 3 == 1:
            with col2:
                if st.button(topic, key=f"btn_{topic}"):
                    st.session_state.page = topic
        else:
            with col3:
                if st.button(topic, key=f"btn_{topic}"):
                    st.session_state.page = topic


def show_topic_page(topic_key: str):
    """Render the page for a selected topic."""
    st.title(topic_key)
    st.markdown(TOPICS[topic_key])

    if st.button("Go Back"):
        st.session_state.page = "main"


def main():
    """Decide which page to show, based on st.session_state.page."""
    if "page" not in st.session_state:
        st.session_state.page = "main"

    current_page = st.session_state.page

    if current_page == "main":
        show_main_page()
    else:
        # If current_page is any topic name, show that topic
        show_topic_page(current_page)


if __name__ == "__main__":
    main()

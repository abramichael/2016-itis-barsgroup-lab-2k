{% extends 'base.html' %}
{% block content %}
    <form action="{% url "login" %}" method="post">
    {% csrf_token %}
    <input type="text" name="username"/>
    <input type="password" name="password"/>
    <input type="submit" value="Sign In"/>
    </form>
{% endblock %}
{{ fullname }}
{{ underline }}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   :inherited-members:
   :special-members: __getitem__, __repr__
   :members:

.. _sphx_glr_backreferences_{{ fullname }}:
.. minigallery:: {{ fullname }}
   :add-heading:

   {% block methods %}
   {% endblock %}

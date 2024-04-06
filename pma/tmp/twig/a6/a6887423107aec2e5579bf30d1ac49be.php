<?php

use Twig\Environment;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Extension\SandboxExtension;
use Twig\Markup;
use Twig\Sandbox\SecurityError;
use Twig\Sandbox\SecurityNotAllowedTagError;
use Twig\Sandbox\SecurityNotAllowedFilterError;
use Twig\Sandbox\SecurityNotAllowedFunctionError;
use Twig\Source;
use Twig\Template;

/* server/user_groups/edit_user_groups.twig */
class __TwigTemplate_32baf4e1947628f60f9ef1eb6bf2c6ab extends Template
{
    private $source;
    private $macros = [];

    public function __construct(Environment $env)
    {
        parent::__construct($env);

        $this->source = $this->getSourceContext();

        $this->parent = false;

        $this->blocks = [
        ];
    }

    protected function doDisplay(array $context, array $blocks = [])
    {
        $macros = $this->macros;
        // line 1
        if ((($context["user_group"] ?? null) == null)) {
            // line 2
            echo "    <h2>";
echo _gettext("Add user group");
            echo "</h2>
";
        } else {
            // line 4
            echo "    <h2>";
            echo twig_escape_filter($this->env, twig_sprintf(_gettext("Edit user group: '%s'"), ($context["edit_user_group_special_chars"] ?? null)), "html", null, true);
            echo "</h2>
";
        }
        // line 6
        echo "<form name=\"userGroupForm\" id=\"userGroupForm\" action=\"";
        echo ($context["user_group_url"] ?? null);
        echo "\" method=\"post\">
    ";
        // line 7
        echo ($context["hidden_inputs"] ?? null);
        echo "
    <fieldset class=\"pma-fieldset\" id=\"fieldset_user_group_rights\">
        <legend>";
echo _gettext("User group menu assignments");
        // line 9
        echo " &nbsp;&nbsp;&nbsp;
            <input type=\"checkbox\" id=\"addUsersForm_checkall\" class=\"checkall_box\" title=\"Check all\">
            <label for=\"addUsersForm_checkall\">";
echo _gettext("Check all");
        // line 11
        echo "</label>
        </legend>
        ";
        // line 13
        if ((($context["user_group"] ?? null) == null)) {
            // line 14
            echo "            <label for=\"userGroup\">";
echo _gettext("Group name:");
            echo "</label>
            <input type=\"text\" name=\"userGroup\" maxlength=\"64\" autocomplete=\"off\" required=\"required\">
            <div class=\"clearfloat\"></div>
        ";
        }
        // line 18
        echo "        ";
        echo ($context["tab_list"] ?? null);
        echo "
    </fieldset>
    <fieldset id=\"fieldset_user_group_rights_footer\" class=\"pma-fieldset tblFooters\">
        <input class=\"btn btn-primary\" type=\"submit\" value=\"";
echo _gettext("Go");
        // line 21
        echo "\">
    </fieldset>
</form>
";
    }

    public function getTemplateName()
    {
        return "server/user_groups/edit_user_groups.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  89 => 21,  81 => 18,  73 => 14,  71 => 13,  67 => 11,  62 => 9,  56 => 7,  51 => 6,  45 => 4,  39 => 2,  37 => 1,);
    }

    public function getSourceContext()
    {
        return new Source("", "server/user_groups/edit_user_groups.twig", "/home/vagrant/proyectos/pma/templates/server/user_groups/edit_user_groups.twig");
    }
}
